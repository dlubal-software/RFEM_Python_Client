Member
========
.. function:: Member(no, start_node_no, end_node_no, rotation_angle, start_section_no, end_section_no, start_member_hinge_no, end_member_hinge_no, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_angle** (*int*): Member Rotation Angle
		* **start_section_no** (*int*): Tag of Start Section
		* **end_section_no** (*int*): Tag of End Section
		* **start_member_hinge_no** (*int*): Tag of Start Member Hinge
		* **end_member_hinge_no** (*int*): Tag of End Member Hinge
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.Beam(no, start_node_no, end_node_no, section_distribution_type, rotation_specification_type, rotation_parameters, start_section_no, end_section_no, distribution_parameters, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **section_distribution_type** (*enum*): Section Distribution Enumeration
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **start_section_no** (*int*): Tag of Start Section
		* **end_section_no** (*int*): Tag of End Section
		* **distribution_parameters** (*list*): Distribution Parameters
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.Rigid(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.Rib(no, start_node_no, end_node_no, section_distribution_type, start_section_no, end_section_no, rib_surfaces_no, rib_alignment, reference_width_type, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **section_distribution_type** (*enum*): Section Distribution Enumeration
		* **start_section_no** (*int*): Tag of Start Section
		* **end_section_no** (*int*): Tag of End Section
		* **rib_surfaces_no** (*list*): Surface Tags Assigned to Rib
		* **rib_alignment** (*enum*): Rib Alignment Enumeration
		* **reference_width_type** (*enum*): Reference Width Enumeration
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.Truss(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, section_no, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **section_no** (*int*): Tag of Section
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.TrussOnlyN(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, section_no, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **section_no** (*int*): Tag of Section
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.Tension(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, section_no, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **section_no** (*int*): Tag of Section
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters

.. function:: Member.Compression(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, section_no, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **section_no** (*int*): Tag of Section
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.Buckling(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, section_no, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **section_no** (*int*): Tag of Section
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.Cable(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, section_no, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **section_no** (*int*): Tag of Section
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.ResultBeam(no, start_node_no, end_node_no, section_distribution_type, rotation_specification_type, rotation_parameters, start_section_no, end_section_no, distribution_parameters, integration_parameters, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **section_distribution_type** (*enum*): Section Distribution Enumeration
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **start_section_no** (*int*): Tag of Start Section
		* **end_section_no** (*int*): Tag of End Section
		* **distribution_parameters** (*list*): Distribution Parameters
		* **integration_parameters** (*list*): Integration Parameters
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.DefinableStiffness(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, definable_stiffness, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **definable_stiffness** (*int*): Tag of Member Definable Stiffness
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.CouplingRigidRigid(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.CouplingRigidHinge(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Member.CouplingHingeRigid(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters

.. function:: Member.CouplingHingeHinge(no, start_node_no, end_node_no, rotation_specification_type, rotation_parameters, comment*, params*)

* Parameters

		* **no** (*int*): Member Tag
		* **start_node_no** (*int*): Tag of Start Node
		* **end_node_no** (*int*): Tag of End Node
		* **rotation_specification_type** (*enum*): Rotation Specification Enumeration
		* **rotation_parameters** (*list*): Rotation Parameters
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters