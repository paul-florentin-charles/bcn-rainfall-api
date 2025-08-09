## Changelog

### v1.0.4
_09/08/2025_

- Use `APIRouter` object to split up routes management.

### v1.0.3
_19/06/2025_

- Add `/graph/standard_deviations` route.

### v1.0.2
_18/06/2025_

- Update `/graph/rainfall_by_year` route to use optional `kmeans_cluster_count` query param.

### v1.0.1
_16/02/2025_

- Add some preliminary tests on FastAPI app object.
  - Add `httpx` package to implement the latter.

### v1.0.0 
_14/02/2025_

- Initial release.
- Code is taken from [this repository](https://github.com/paul-florentin-charles/bcn-rainfall-models).