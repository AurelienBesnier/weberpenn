
# This file has been generated at Mon Sep  6 10:50:55 2010

from openalea.core import *


__name__ = 'demo.weberpenn'

__editable__ = True
__description__ = 'Demonstration of the WeberPenn geometric model.'
__license__ = 'CECILL'
__url__ = ''
__alias__ = []
__version__ = '0.1.5'
__authors__ = 'Christophe Pradal'
__institutes__ = 'CIRAD'
__icon__ = 'icon.png'


__all__ = ['_178248236', '_178249004', '_178249676']



_178248236 = CompositeNodeFactory(name='demo_WeberPenn_grp_1',
                             description='',
                             category='composite, demo',
                             doc='',
                             inputs=[  {  'interface': None, 'name': 'seed(weber and penn)', 'value': None},
   {  'interface': None, 'name': 'position(weber and penn)', 'value': None},
   {  'interface': None,
      'name': 'global_params(tree parameters)',
      'value': {  'base_size': 0.29999999999999999,
                  'base_split': 0,
                  'flare': None,
                  'leaf_scale': 0.59999999999999998,
                  'leaf_scale_x': 1.0,
                  'leaves': 0,
                  'lobes': None,
                  'lobes_variance': None,
                  'order': 3,
                  'ratio': 0.02,
                  'ratio_power': 0.80000000000000004,
                  'scale': 20.0,
                  'scale_variance': 2.0,
                  'shape_id': 0}},
   {  'interface': None,
      'name': 'order0(tree parameters)',
      'value': {  'branches': 20,
                  'curve': 20.0,
                  'curve_back': -20.0,
                  'curve_res': 5,
                  'curve_variance': 0.0,
                  'down_angle': 30.0,
                  'down_angle_variance': 0.0,
                  'length': 1.0,
                  'length_variance': 0.0,
                  'rotate': 137.0,
                  'rotate_variance': 0.0,
                  'seg_split': 0.0,
                  'split_angle': 0.0,
                  'split_angle_variance': 0.0}},
   {  'interface': None,
      'name': 'order1(tree parameters)',
      'value': {  'branches': 10,
                  'curve': 30.0,
                  'curve_back': -40.0,
                  'curve_res': 5,
                  'curve_variance': 30.0,
                  'down_angle': 80.0,
                  'down_angle_variance': 0.0,
                  'length': 0.40000000000000002,
                  'length_variance': 0.0,
                  'rotate': 130.0,
                  'rotate_variance': 0.0,
                  'seg_split': 0.0,
                  'split_angle': 0.0,
                  'split_angle_variance': 0.0}},
   {  'interface': None,
      'name': 'order2(tree parameters)',
      'value': {  'branches': 10,
                  'curve': 20.0,
                  'curve_back': -20.0,
                  'curve_res': 5,
                  'curve_variance': -40.0,
                  'down_angle': 40.0,
                  'down_angle_variance': 0.0,
                  'length': 0.5,
                  'length_variance': 0.0,
                  'rotate': 90.0,
                  'rotate_variance': 0.0,
                  'seg_split': 0.0,
                  'split_angle': 0.0,
                  'split_angle_variance': 0.0}},
   {  'interface': None,
      'name': 'order3(tree parameters)',
      'value': {  'branches': 10,
                  'curve': 20.0,
                  'curve_back': -20.0,
                  'curve_res': 5,
                  'curve_variance': -40.0,
                  'down_angle': 40.0,
                  'down_angle_variance': 0.0,
                  'length': 0.5,
                  'length_variance': 0.0,
                  'rotate': 90.0,
                  'rotate_variance': 0.0,
                  'seg_split': 0.0,
                  'split_angle': 0.0,
                  'split_angle_variance': 0.0}}],
                             outputs=[{  'interface': None, 'name': 'out(weber and penn)'}],
                             elt_factory={  8: ('vplants.weberpenn', 'tree parameters'),
   10: ('vplants.weberpenn', 'weber and penn')},
                             elt_connections={  152804764: ('__in__', 2, 8, 0),
   152804776: (8, 0, 10, 0),
   152804788: (10, 0, '__out__', 0),
   152804800: ('__in__', 1, 10, 2),
   152804812: ('__in__', 0, 10, 1),
   152804824: ('__in__', 4, 8, 2),
   152804836: ('__in__', 3, 8, 1),
   152804848: ('__in__', 6, 8, 4),
   152804860: ('__in__', 5, 8, 3)},
                             elt_data={  8: {  'block': False,
         'caption': 'tree parameters',
         'delay': 0,
         'factory': '<openalea.core.node.NodeFactory object at 0xa6e72cc> : "tree parameters"',
         'hide': True,
         'id': 8,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 67.013254113345567,
         'posy': 34.796617915904982,
         'priority': 0,
         'use_user_color': False,
         'user_application': None,
         'user_color': None},
   10: {  'block': False,
          'caption': 'weber and penn',
          'delay': 0,
          'factory': '<openalea.core.node.NodeFactory object at 0xa6e74ac> : "weber and penn"',
          'hide': True,
          'id': 10,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': 10.418190127970803,
          'posy': 82.132084095064045,
          'priority': 0,
          'use_user_color': False,
          'user_application': None,
          'user_color': None},
   '__in__': {  'block': False,
                'caption': 'In',
                'delay': 0,
                'hide': True,
                'id': 0,
                'lazy': True,
                'port_hide_changed': set(),
                'posx': 55.0,
                'posy': -46.5,
                'priority': 0,
                'use_user_color': False,
                'user_application': None,
                'user_color': None},
   '__out__': {  'block': False,
                 'caption': 'Out',
                 'delay': 0,
                 'hide': True,
                 'id': 1,
                 'lazy': True,
                 'port_hide_changed': set(),
                 'posx': 52.184643510054833,
                 'posy': 130.46983546617915,
                 'priority': 0,
                 'use_user_color': False,
                 'user_application': None,
                 'user_color': None}},
                             elt_value={  8: [], 10: [], '__in__': [], '__out__': []},
                             elt_ad_hoc={  8: {'position': [67.013254113345567, 34.796617915904982], 'userColor': None, 'useUserColor': False},
   10: {'position': [10.418190127970803, 82.132084095064045], 'userColor': None, 'useUserColor': False},
   '__in__': {'position': [55.0, -46.5], 'userColor': None, 'useUserColor': False},
   '__out__': {'position': [52.184643510054833, 130.46983546617915], 'userColor': None, 'useUserColor': False}},
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_178249004 = CompositeNodeFactory(name='test_quakingaspen',
                             description='',
                             category='demo,composite',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('vplants.plantgl.visualization', 'plot3D'),
   3: ('system', 'annotation'),
   4: ('vplants.weberpenn', 'weber and penn'),
   5: ('vplants.weberpenn', 'order parameters'),
   6: ('vplants.weberpenn', 'species'),
   7: ('vplants.weberpenn', 'order parameters'),
   8: ('vplants.weberpenn', 'tree parameters'),
   9: ('vplants.weberpenn', 'global parameters'),
   10: ('vplants.weberpenn', 'weber and penn'),
   11: ('vplants.weberpenn', 'order parameters'),
   12: ('vplants.plantgl.visualization', 'plot3D'),
   13: ('openalea.data structure', 'int'),
   14: ('system', 'annotation'),
   15: ('system', 'annotation'),
   16: ('system', 'annotation'),
   17: ('vplants.weberpenn', 'quaking aspen'),
   18: ('vplants.weberpenn', 'tree parameters'),
   19: ('openalea.data structure', 'int')},
                             elt_connections={  9779692: (6, 0, 4, 0),
   9779704: (11, 0, 8, 2),
   9779716: (7, 0, 8, 1),
   9779728: (8, 0, 10, 0),
   9779740: (13, 0, 4, 1),
   9779752: (19, 0, 10, 1),
   9779764: (10, 0, 12, 0),
   9779776: (5, 0, 8, 3),
   9779788: (9, 0, 8, 0),
   9779800: (4, 0, 2, 0),
   9779812: (5, 0, 8, 4)},
                             elt_data={  2: {  'block': False,
         'caption': 'plot3D',
         'hide': True,
         'lazy': False,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 607.7314814814813,
         'posy': 424.38271604938268,
         'priority': 0,
         'user_application': False},
   3: {  'posx': 38.75,
         'posy': 238.75,
         'txt': 'Geometric parameters:\n  * length of axes\n  * curvature\n  * phyllotaxis\n  * insertion angle\n\nTopologic parameters:\n  * number of branches'},
   4: {  'block': False,
         'caption': 'weber and penn',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 571.25,
         'posy': 353.75,
         'priority': 0,
         'user_application': None},
   5: {  'block': False,
         'caption': 'order2',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([6, 7, 8]),
         'posx': 408.75,
         'posy': 168.75,
         'priority': 0,
         'user_application': None},
   6: {  'block': False,
         'caption': 'species',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 708.75,
         'posy': 142.5,
         'priority': 0,
         'user_application': None},
   7: {  'block': False,
         'caption': 'trunk',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([4, 6, 7, 8, 10, 12]),
         'posx': 173.75,
         'posy': 170.0,
         'priority': 0,
         'user_application': None},
   8: {  'block': False,
         'caption': 'tree parameters',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 408.75,
         'posy': 283.75,
         'priority': 0,
         'user_application': None},
   9: {  'block': False,
         'caption': 'global parameters',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': -2.5,
         'posy': 123.75,
         'priority': 0,
         'user_application': None},
   10: {  'block': False,
          'caption': 'weber and penn',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': 396.25,
          'posy': 368.75,
          'priority': 0,
          'user_application': None},
   11: {  'block': False,
          'caption': 'order1',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set([6, 7, 8]),
          'posx': 258.75,
          'posy': 92.5,
          'priority': 0,
          'user_application': None},
   12: {  'block': False,
          'caption': 'plot3D',
          'hide': True,
          'lazy': False,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': 429.65343855358697,
          'posy': 428.77617885113841,
          'priority': 0,
          'user_application': True},
   13: {  'block': False,
          'caption': '1',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': 765.0,
          'posy': 253.75,
          'priority': 0,
          'user_application': None},
   14: {  'posx': 636.25,
          'posy': 93.75,
          'txt': 'Predefined parameters for specific species'},
   15: {  'posx': 613.75,
          'posy': -22.5,
          'txt': 'Plant simulation with weber & penn method'},
   16: {  'posx': 616.25, 'posy': 11.25, 'txt': 'Author : Christophe Pradal'},
   17: {  'block': False,
          'caption': 'quaking aspen',
          'hide': True,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 216.25,
          'posy': 732.5,
          'priority': 0,
          'user_application': None},
   18: {  'block': False,
          'caption': 'tree parameters',
          'hide': True,
          'lazy': True,
          'port_hide_changed': set(),
          'posx': 197.5,
          'posy': 995.0,
          'priority': 0,
          'user_application': None},
   19: {  'block': False,
          'caption': '27',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': 558.75,
          'posy': 281.25,
          'priority': 0,
          'user_application': None},
   '__in__': {  'caption': 'In',
                'hide': True,
                'lazy': True,
                'minimal': False,
                'port_hide_changed': set(),
                'posx': 20.0,
                'posy': 5.0,
                'priority': 0},
   '__out__': {  'caption': 'Out',
                 'hide': True,
                 'lazy': True,
                 'minimal': False,
                 'port_hide_changed': set(),
                 'posx': 20.0,
                 'posy': 250.0,
                 'priority': 0}},
                             elt_value={  2: [],
   3: [],
   4: [(2, 'None')],
   5: [  (0, '0.59999999999999998'),
         (1, '0.0'),
         (2, '3'),
         (3, '-40.0'),
         (4, '0.0'),
         (5, '75.0'),
         (6, '0.0'),
         (7, '0.0'),
         (8, '0.0'),
         (9, '45.0'),
         (10, '10.0'),
         (11, '78.0'),
         (12, '0.0'),
         (13, '15')],
   6: [(0, "'Quaking Aspen'")],
   7: [  (0, '1.0'),
         (1, '0.0'),
         (2, '3'),
         (3, '0.0'),
         (4, '0.0'),
         (5, '20.0'),
         (6, '0.0'),
         (7, '0.0'),
         (8, '0.0'),
         (9, '0.0'),
         (10, '0.0'),
         (11, '140.0'),
         (12, '0.0'),
         (13, '35')],
   8: [],
   9: [  (0, "'7 - Tend Flame'"),
         (1, '0.40000000000000002'),
         (2, '8.0'),
         (3, '2.0'),
         (4, '3'),
         (5, '0.01'),
         (6, '0.80000000000000004'),
         (7, '10'),
         (8, '0.22'),
         (9, '1.0'),
         (10, 'None'),
         (11, 'None'),
         (12, 'None'),
         (13, '0')],
   10: [(2, 'None')],
   11: [  (0, '0.34999999999999998'),
          (1, '0.0'),
          (2, '5'),
          (3, '-40.0'),
          (4, '0.0'),
          (5, '50.0'),
          (6, '0.0'),
          (7, '0.0'),
          (8, '0.0'),
          (9, '60.0'),
          (10, '-10.0'),
          (11, '140.0'),
          (12, '0.0'),
          (13, '13')],
   12: [],
   13: [(0, '4')],
   14: [],
   15: [],
   16: [],
   17: [],
   18: [(0, 'None'), (1, 'None'), (2, 'None'), (3, 'None'), (4, 'None')],
   19: [(0, '27')],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  },
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




_178249676 = CompositeNodeFactory(name='demo_WeberPenn',
                             description='Weber and Penn model for tree generation',
                             category='demo,composite',
                             doc='',
                             inputs=[],
                             outputs=[],
                             elt_factory={  2: ('PlantGL.Visualization', 'plot3D'),
   3: ('System', 'annotation'),
   4: ('WeberPenn', 'weber and penn'),
   5: ('WeberPenn', 'order parameters'),
   6: ('WeberPenn', 'species'),
   7: ('WeberPenn', 'order parameters'),
   8: ('WeberPenn', 'tree parameters'),
   9: ('WeberPenn', 'global parameters'),
   10: ('WeberPenn', 'weber and penn'),
   11: ('WeberPenn', 'order parameters'),
   12: ('PlantGL.Visualization', 'plot3D'),
   13: ('Catalog.Data', 'int'),
   14: ('System', 'annotation'),
   15: ('System', 'annotation'),
   16: ('System', 'annotation')},
                             elt_connections={  9789640: (11, 0, 8, 2),
   9789652: (8, 0, 10, 0),
   9789664: (4, 0, 2, 0),
   9789676: (7, 0, 8, 1),
   9789688: (5, 0, 8, 3),
   9789700: (10, 0, 12, 0),
   9789712: (9, 0, 8, 0),
   9789724: (13, 0, 4, 1),
   9789736: (5, 0, 8, 4),
   9789748: (6, 0, 4, 0)},
                             elt_data={  2: {  'caption': 'plot3D',
         'hide': True,
         'lazy': False,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 606.4814814814813,
         'posy': 424.38271604938274,
         'priority': 0},
   3: {  'posx': 38.75,
         'posy': 238.75,
         'txt': 'Geometric parameters:\n  * length of axes\n  * curvature\n  * phyllotaxis\n  * insertion angle\n\nTopologic parameters:\n  * number of branches'},
   4: {  'caption': 'weber and penn',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 571.25,
         'posy': 353.75,
         'priority': 0},
   5: {  'caption': 'order2',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([6, 7, 8]),
         'posx': 408.75,
         'posy': 168.75,
         'priority': 0},
   6: {  'caption': 'species',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 708.75,
         'posy': 142.5,
         'priority': 0},
   7: {  'caption': 'trunk',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set([4, 6, 7, 8, 10, 12]),
         'posx': 173.75,
         'posy': 170.0,
         'priority': 0},
   8: {  'caption': 'tree parameters',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': 408.75,
         'posy': 283.75,
         'priority': 0},
   9: {  'caption': 'global parameters',
         'hide': True,
         'lazy': True,
         'minimal': False,
         'port_hide_changed': set(),
         'posx': -2.5,
         'posy': 123.75,
         'priority': 0},
   10: {  'caption': 'weber and penn',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': 396.25,
          'posy': 368.75,
          'priority': 0},
   11: {  'caption': 'order1',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set([6, 7, 8]),
          'posx': 258.75,
          'posy': 92.5,
          'priority': 0},
   12: {  'caption': 'plot3D',
          'hide': True,
          'lazy': False,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': 428.40343855358691,
          'posy': 430.02617885113847,
          'priority': 0},
   13: {  'caption': '99',
          'hide': True,
          'lazy': True,
          'minimal': False,
          'port_hide_changed': set(),
          'posx': 738.75,
          'posy': 315.0,
          'priority': 0},
   14: {  'posx': 636.25,
          'posy': 93.75,
          'txt': 'Predefined parameters for specific species'},
   15: {  'posx': 613.75,
          'posy': -22.5,
          'txt': 'Plant simulation with weber & penn method'},
   16: {  'posx': 616.25, 'posy': 11.25, 'txt': 'Author : Christophe Pradal'},
   '__in__': {  'caption': 'In',
                'hide': True,
                'lazy': True,
                'minimal': False,
                'port_hide_changed': set(),
                'posx': 20.0,
                'posy': 5.0,
                'priority': 0},
   '__out__': {  'caption': 'Out',
                 'hide': True,
                 'lazy': True,
                 'minimal': False,
                 'port_hide_changed': set(),
                 'posx': 20.0,
                 'posy': 250.0,
                 'priority': 0}},
                             elt_value={  2: [],
   3: [],
   4: [(2, 'None')],
   5: [  (0, '0.5'),
         (1, '0.0'),
         (2, '5'),
         (3, '20.0'),
         (4, '-40.0'),
         (5, '-20.0'),
         (6, '0.0'),
         (7, '0.0'),
         (8, '0.0'),
         (9, '40.0'),
         (10, '0.0'),
         (11, '90.0'),
         (12, '0.0'),
         (13, '10')],
   6: [(0, "'Black Tupelo'")],
   7: [  (0, '1.0'),
         (1, '0.0'),
         (2, '5'),
         (3, '20.0'),
         (4, '0.0'),
         (5, '-20.0'),
         (6, '0.0'),
         (7, '0.0'),
         (8, '0.0'),
         (9, '30.0'),
         (10, '0.0'),
         (11, '137.0'),
         (12, '0.0'),
         (13, '20')],
   8: [],
   9: [  (0, "'0 - Conical'"),
         (1, '0.29999999999999999'),
         (2, '20.0'),
         (3, '2.0'),
         (4, '3'),
         (5, '0.02'),
         (6, '0.80000000000000004'),
         (7, '0'),
         (8, '0.59999999999999998'),
         (9, '1.0'),
         (10, 'None'),
         (11, 'None'),
         (12, 'None'),
         (13, '0')],
   10: [(1, 'None'), (2, 'None')],
   11: [  (0, '0.40000000000000002'),
          (1, '0.0'),
          (2, '5'),
          (3, '30.0'),
          (4, '30.0'),
          (5, '-40.0'),
          (6, '0.0'),
          (7, '0.0'),
          (8, '0.0'),
          (9, '80.0'),
          (10, '0.0'),
          (11, '130.0'),
          (12, '0.0'),
          (13, '10')],
   12: [],
   13: [(0, '99')],
   14: [],
   15: [],
   16: [],
   '__in__': [],
   '__out__': []},
                             elt_ad_hoc={  },
                             lazy=True,
                             eval_algo='LambdaEvaluation',
                             )




