from package_utils.context import Context

from super_repository.models import Config, Options, Secrets

context = Context(Options, Config, Secrets)
