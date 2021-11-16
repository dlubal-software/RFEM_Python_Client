Line
===========
.. function:: Line(no, nodes_no, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters

.. function:: Line.Polyline(no, nodes_no, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters

.. function:: Line.Arc(no, nodes_no, control_point, alpha_adjustment_target, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **control_point** (*list*): Coordinates of the Control Point
		* **alpha_adjustment_target** (*enum*): Line Arc Alpha Adjustment Target
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Line.Circle(no, nodes_no, center_of_cirle, circle_radius, point_of_normal_to_circle_plane, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **center_of_cirle** (*list*): Coordinates of the Center Point
		* **circle_radius** (*float*): Radius of the Circle
		* **point_of_normal_to_circle_plane** (*list*): Coordinates of the Normal Point
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Line.EllipticalArc(no, nodes_no, p1_control_point, p2_control_point, p3_control_point, arc_angle_alpha, arc_angle_beta, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **p1_control_point** (*list*): Coordinates of the Control Point 1
		* **p2_control_point** (*list*): Coordinates of the Control Point 2
		* **p3_control_point** (*list*): Coordinates of the Control Point 3
		* **arc_angle_alpha** (*float*): Alpha Angle
		* **arc_angle_beta** (*float*): Beta Angle
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Line.Ellipse(no, nodes_no, p3_control_point, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **p3_control_point** (*list*): Coordinates of the Control Point 3
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Line.Parabola(no, nodes_no, p3_control_point, parabola_alpha, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **p3_control_point** (*list*): Coordinates of the Control Point 3
		* **parabola_alpha** (*float*): Alpha Angle
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters

.. function:: Line.Spline(no, nodes_no, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters
		
.. function:: Line.NURBS(no, nodes_no, control_points, weights, comment*, params*)

* Parameters

		* **no** (*int*): Line Tag
		* **nodes_no** (*str*): Tags of Nodes
		* **control_points** (*list*): List of Coordinates of the Control Points
		* **weights** (*list*): List of Weights
		* **comment** ( *str, optional*): Comments
		* **params** (*dict, optional*): Parameters