from pystratum.mssql.wrapper.Wrapper import Wrapper


# ----------------------------------------------------------------------------------------------------------------------
class Singleton0Wrapper(Wrapper):
    # ------------------------------------------------------------------------------------------------------------------
    def _write_result_handler(self, routine):
        self._write_line('return StaticDataLayer.execute_singleton0(%s)' % self._generate_command(routine))


# ----------------------------------------------------------------------------------------------------------------------
