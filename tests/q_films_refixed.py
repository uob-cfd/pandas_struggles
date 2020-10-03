test = {
  'name': 'Question films_refixed',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'films_refixed'
          >>> 'films_refixed' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'films_refixed'
          >>> # from its initial state (of ...)
          >>> films_refixed is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(films_refixed, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> films_refixed.shape
          (33, 5)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> films_refixed['Votes'].dtype.type == np.float64
          True
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
