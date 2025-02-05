# PyPaf

Formats the elements of a Royal Mail Postcode Address File entry according to the rules described in the [Royal Mail Programmer's Guide Edition 7, Version 6.2](https://www.poweredbypaf.com/wp-content/uploads/2024/11/Latest-Programmers_guide_Edition-7-Version-6-2.pdf)

## Installation

Install it from PyPI:

    pip install pypaf

## Usage

May be used to format the PAF Address elements as an array of strings:

```python
import paf
address = paf.Address({
    'building_name': "1-2",
    'thoroughfare_name': "NURSERY",
    'thoroughfare_descriptor': "LANE",
    'dependent_locality': "PENN",
    'post_town': "HIGH WYCOMBE",
    'postcode': "HP10 8LS"
})
address.list() # or list(address)

['1-2 NURSERY LANE', 'PENN', 'HIGH WYCOMBE', 'HP10 8LS']
```

Or as a single string:

```python
import paf
address = paf.Address({
    'building_name': "1-2",
    'thoroughfare_name': "NURSERY",
    'thoroughfare_descriptor': "LANE",
    'dependent_locality': "PENN",
    'post_town': "HIGH WYCOMBE",
    'postcode': "HP10 8LS"
})
address.str() # or str(address)

'1-2 NURSERY LANE, PENN, HIGH WYCOMBE. HP10 8LS'
```

## Development

After checking out the repo, run `pytest` to run the tests.

To release a new version, update the version number in `version.py`, and then run `python -m build`, which will create a distribution archive. Run `python -m twine upload dist/*`, to upload the distribution archive to [pypi.org](https://pypi.org).

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/drabjay/pypaf. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The package is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

## Code of Conduct

Everyone interacting in the PyPaf project’s codebases, issue trackers, chat rooms and mailing lists is expected to follow the [code of conduct](https://github.com/drabjayc/pypaf/blob/master/CODE_OF_CONDUCT.md).