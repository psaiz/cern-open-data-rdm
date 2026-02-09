"""JS/CSS Webpack bundles for Open Data RDM."""

from invenio_assets.webpack import WebpackThemeBundle, WebpackBundle

theme = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "cernopendata_css": "./scss/styles.scss",
                "cernopendata_js": "./js/app.js",
            },
            dependencies={
                "open-iconic": "~1.1.1",
                "popper.js": "~1.11.0",
                "recharts": "^1.8.5",
            },
        ),
    },
)

glossary = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "glossary_js": "./js/glossary/jquery.zglossary.jsasdas",
                "glossary_css": "./js/glossary/jquery.zglossary.cssdsasdas",
            },
        )
    },
)