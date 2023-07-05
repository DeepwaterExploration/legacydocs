# DeepWater Exploration Documentation Site

[DWE Documentation Site](https://docs.exploredeepwater.com)

## Developing

> The [MyST-Markdown](https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight) extension is recommended for development.

1. Clone the project: `git clone https://github.com/DeepwaterExploration/DeepwaterExplorationDocs.git`
2. cd to the docs directory: `cd DeepwaterExplorationDocs/docs`
2. Install the requirments: `pip install -r requirements.txt` (you may need to use an administrator shell)
4. Run the live server: `sphinx-autobuild . build/html`. When a change is detected in `build/html`, the documentation is rebuilt and any open browser windows are reloaded automatically. `KeyboardInterrupt` (<kbd>ctrl</kbd>+<kbd>c</kbd>) will stop the server.
5. Open the browser to view the local server: `http://localhost:8000`

## Structure

- `docs/index.rst` - index file (written in reStructuredText)
- `docs/*.md` - myST markdown files (new ones should be added to the `index.rst` table of contents)
- `docs/conf.py` - site configuration (only modified when absolutely necessary)

## Contributing

1. Fork the project
2. Create your feature branch `git checkout -b feature/AmazingFeature`
3. Commit your changes `git commit -m "Add some amazing feature"`
4. Push to the branch `git push origin feature/AmazingFeature`
5. Open a Pull Request
