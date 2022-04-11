Create and Acces Files
========================

To ensure sufficient connectivity between client and server, the following should be considered. Web Services functionality within RFEM6/RSTAB9 needs to be activated. 
To do this, enable the “Start the server automatically with the application” dialog box under “Program Options”.

Furthermore, an active instance of RFEM6/RSTAB9 needs to be opened before attempting any sort of interaction. This, simply said, means opening the program.

Interaction with and instructions to the software logically occurs between a begin_modifcation() and finish_modification() function call. This is illustrated below::

   Model.clientModel.service.begin_modification('new')


   ------------(your interaction)------------


   Model.clientModel.service.finish_modification()

Since multiple model instances be running, the method to manage this effectively is described below. Creating new models or editing existing models can be controlled via Model() class.

* If there is no open model in RFEM, it can be created with::

   Model(True, "MyModel")


   Model.clientModel.service.begin_modification('new')


   Model.clientModel.service.finish_modification()

* If there is one model opened in RFEM, it can be edited with::

   Model(False)

   Model.clientModel.service.begin_modification('new')

   Model.clientModel.service.finish_modification()

* If there is multiple models opened in RFEM, one can be edited with::

   Model(False, "model_name")


   Model.clientModel.service.begin_modification('new')


   Model.clientModel.service.finish_modification()