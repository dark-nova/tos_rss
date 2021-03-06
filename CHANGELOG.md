# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [2.0.2] - 2019-09-09
### Changed
- `feed.py` renamed to `generate_feed.py`
- When entries could not be generated, don't overwrite the feed

## [2.0.1] - 2019-09-01
### Added
- Add [license](LICENSE)

### Changed
- Updated [readme](README.md)

## [2.0] - 2019-08-27
### Added
- Retroactively add a changelog
- Include a [`README.md`](README.md) to describe the project
- Include an [example](example.html)
- Use `sqlite3` to manage publication times where none exist on the page
    - Add a [`db.py`](db.py) to manage the database

### Changed
- Use `feedgen` instead of `rfeed` - #1

## [1.0.1] - 2019-06-24
### Changed
- Move `feed.xml` into [`feed.xml.original`](feed.xml.original) as baseline
- Untrack `feed.xml` as it changes instead

## [1.0] - 2019-04-12
### Added
- Initial version
