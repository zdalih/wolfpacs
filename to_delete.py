from pydicom.dataset import Dataset

from pnd3.pynetdicom3 import AE
from pnd3.pynetdicom3 import QueryRetrieveSOPClassList

# QueryRetrieveSOPClassList contains the SOP Classes supported
#   by the Query/Retrieve Service Class (see PS3.4 Annex C.6)
ae = AE(scu_sop_class=QueryRetrieveSOPClassList)

# Try and associate with the peer AE
#   Returns the Association thread
print('Requesting Association with the peer')
assoc = ae.associate('88.202.185.144', 11112)

if assoc.is_established:
    print('Association accepted by the peer')

    # Creat a new DICOM dataset with the attributes to match against
    #   In this case match any patient's name at the PATIENT query
    #   level. See PS3.4 Annex C.6 for the complete list of possible
    #   attributes and query levels.
    dataset = Dataset()
    dataset.PatientName = 'Bowen'

    # Send a DIMSE C-FIND request to the peer
    #   query_model is the Query/Retrieve Information Model to use
    #   and is one of 'W', 'P', 'S', 'O'
    #       'W' - Modality Worklist (1.2.840.10008.5.1.4.31)
    #       'P' - Patient Root (1.2.840.10008.5.1.4.1.2.1.1)
    #       'S' - Study Root (1.2.840.10008.5.1.4.1.2.2.1)
    #       'O' - Patient/Study Only (1.2.840.10008.5.1.4.1.2.3.1)
    responses = assoc.send_c_find(dataset, query_model='P')

    for (status, dataset) in responses:
        # While status is pending we should get the matching datasets
        if status == 'Pending':
            print(dataset)
        elif status == 'Success':
            print('C-FIND finished, releasing the association')
        elif status == 'Cancel':
            print('C-FIND cancelled, releasing the association')
        elif status == 'Failure':
            print('C-FIND failed, releasing the association')


    # Release the association
    assoc.release()

