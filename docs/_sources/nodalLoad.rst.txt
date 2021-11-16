Nodal Load
===========
.. function:: NodalLoad(no, load_case_no, nodes_no, load_direction, magnitude, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **load_case_no** (*int*): Load Case No
		* **nodes_no** (*str*): Tags of Nodes
		* **load_direction** (*enum*): Load Direction Enumeration
		* **magnitude** (*float*): Load Magnitude
		* **comment** (*str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		

.. function:: NodalLoad.Force(no, load_case_no, nodes_no, load_direction, magnitude, force_eccentricity, specific_direction, shifted_display, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **load_case_no** (*int*): Load Case No
		* **nodes_no** (*str*): Tags of Nodes
		* **comment** ( *str, optional*): Comments
		* **load_direction** (*enum*): Load Direction Enumeration
		* **magnitude** (*float*): Load Magnitude
		* **force_eccentricity** (*bool*): Force Eccentricity Option
		* **specific_direction** (*bool*): Specific Direction Option
		* **shifted_display** (*bool*): Shifted Display Option
		* **comment** (*str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
