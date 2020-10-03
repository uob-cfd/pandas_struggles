test = {
  'name': 'Question dump_colons',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> dump_colons('32')
          32
          >>> dump_colons('901')
          901
          >>> dump_colons('901:3')
          nan
          >>> dump_colons('1:30')
          nan
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> dump_colons('-3')
          -3
          >>> dump_colons('-9')
          -9
          >>> dump_colons(':')
          nan
          >>> dump_colons('anthing:at:all')
          nan
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
