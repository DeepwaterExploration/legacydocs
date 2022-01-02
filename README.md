# DeepWater Exploration Documentation Site

[https://docs.exploredeepwater.com](https://docs.exploredeepwater.com)

## Developing

1. Clone the project: `git clone https://github.com/DeepwaterExploration/DeepwaterExplorationDocs.git`
2. cd to the docs directory: `cd DeepwaterExplorationDocs/docs`
2. Install the requirments: `pip install -r requirements.txt` (you may need to use an administrator shell)
4. Run the live server: `sphinx-autobuild . build/html`

## Structure

- `docs/index.rst` - index file restructured text
- `docs/*.md` - myST markdown files (new ones should be added to the index.rst table of contents)
- `docs/conf.py` - configuration for the site (should not be changed unless absolutely necessary)

## Contributing

1. Fork the project
2. Create your feature branch `git checkout -b feature/AmazingFeature`
3. Commit your changes `git commit -m "Add some amazing feature""`
4. Push to the branch `git push origin feature/AmazingFeature`
5. Open a Pull Request
