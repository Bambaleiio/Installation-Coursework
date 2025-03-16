from __ServerLibs import _ServerLibs

class _InternetLibs:
    @staticmethod
    def installed(libs: list[str]) -> dict[str, bool]:
        return _ServerLibs.installed(libs)

    @staticmethod
    def installed_all(libs: list[str]) -> bool:
        return all(_ServerLibs.installed(libs).values())

    @staticmethod
    def install(packages: list[str]) -> None:
        _ServerLibs.install(packages)

