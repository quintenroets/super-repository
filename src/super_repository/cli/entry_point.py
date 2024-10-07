from package_utils.context.entry_point import create_entry_point

from super_repository import main
from super_repository.context import context

entry_point = create_entry_point(main, context)
