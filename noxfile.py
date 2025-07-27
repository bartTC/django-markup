import nox

# Define Python versions to test against
PYTHON_VERSIONS = ["3.9", "3.10", "3.11", "3.12", "3.13"]

# Define Django versions to test against
DJANGO_VERSIONS = {
    "django-32": "django==3.2.*",
    "django-42": "django==4.2.*",
    "django-50": "django==5.0.*",
    "django-51": "django==5.1.*",
    "django-52": "django==5.2.*",
}

# Define which Python versions can be used with which Django versions
DJANGO_PYTHON_COMPATIBILITY = {
    "django-32": ["3.9", "3.10", "3.11", "3.12", "3.13"],
    "django-42": ["3.9", "3.10", "3.11", "3.12", "3.13"],
    "django-50": ["3.10", "3.11", "3.12", "3.13"],
    "django-51": ["3.10", "3.11", "3.12", "3.13"],
    "django-52": ["3.10", "3.11", "3.12", "3.13"],
}

# Configure nox
nox.options.sessions = ["tests"]
nox.options.reuse_existing_virtualenvs = False
nox.options.error_on_missing_interpreters = False


@nox.session(python=PYTHON_VERSIONS)
@nox.parametrize("django", list(DJANGO_VERSIONS.keys()))
def tests(session: nox.sessions.Session, django: str) -> None:
    """Run the test suite with pytest."""
    # Skip incompatible Python-Django combinations
    if session.python not in DJANGO_PYTHON_COMPATIBILITY[django]:
        session.skip(f"Python {session.python} not compatible with {django}")

    # Set environment variables
    session.env["DJANGO_SETTINGS_MODULE"] = "django_markup.tests.settings"

    # Install dependencies
    session.install("poetry-core>=2")
    session.install("pytest", "pytest-django", "pytest-cov")
    session.install(DJANGO_VERSIONS[django])

    # Install the package with all filter dependencies
    session.install("-e", ".[all_filter_dependencies]")

    # Run pytest
    session.run("pytest")
