import nox
from nox.sessions import Session

locations = "src"
nox.options.sessions = "blacken"
nox.options.stop_on_first_error = True


@nox.session(python=["3.8"], reuse_venv=True)
def blacken(session: Session) -> None:
    """
    Run black code formatter
    """
    args = session.posargs or locations
    session.install("black==20.8b1", "isort==5.6.4")
    session.run("isort", *args)
    session.run("black", *args)
