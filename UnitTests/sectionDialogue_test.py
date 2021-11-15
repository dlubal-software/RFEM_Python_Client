import sys
sys.path.append(".")
from RFEM.enums import *
from RFEM.baseSettings import *
from RFEM.Tools.sectionDialogue import *

if __name__ == '__main__':  
    clientModel.service.begin_modification()

    # Create section favorite lists
    SectionDialogue.CreateSectionFavoriteList(0, 'Favs_1')
    SectionDialogue.CreateSectionFavoriteList(0, 'Favs_2')

    # Add section to favorite list
    SectionDialogue.AddSectionToFavoriteList(0, 'Favs_1', 'IPE 300')
    SectionDialogue.AddSectionToFavoriteList(0, 'Favs_1', 'HEA 200')

    # Delete section from favorite list
    SectionDialogue.DeleteSectionFromFavoriteList(0, 'Favs_1', 'HEA 200')
    
    # Delete section favorite list
    SectionDialogue.DeleteSectionFavoriteList(0, 'Favs_2')

    # Get section favorite lists
    section_favorite_lists = SectionDialogue.GetSectionFavoriteLists(0)
    print(dict(section_favorite_lists))

    # Create section from rsection file
    SectionDialogue.CreateSectionFromRsectionFile(0, 3, 'rsc_file_path')

    clientModel.service.finish_modification()