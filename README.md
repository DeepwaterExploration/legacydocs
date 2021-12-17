# DeepWater Exploration Documentation Site

## Developing

`sphinx-autobuild . build/html`

## Releasing

`make html && rm -rf /var/docs/* && mkdir /var/docs/html && cp ./build/html/* /var/docs/html/ -r`
