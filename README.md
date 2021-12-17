# DeepWater Exploration Documentation Site

[https://docs.exploredeepwater.com](https://docs.exploredeepwater.com)

## Developing

`sphinx-autobuild . build/html`

## Releasing

`make html && rm -rf /var/docs/* && mkdir /var/docs/html && cp ./build/html/* /var/docs/html/ -r`
