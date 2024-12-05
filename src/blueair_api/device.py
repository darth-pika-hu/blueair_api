import dataclasses
import logging

from .callbacks import CallbacksMixin
from .http_blueair import HttpBlueair

_LOGGER = logging.getLogger(__name__)

@dataclasses.dataclass(slots=True)
class Device(CallbacksMixin):
    api: HttpBlueair
    uuid: str | None = None
    name: str | None = None
    timezone: str | None = None
    compatibility: str | None = None
    model: str | None = None
    mac: str | None = None
    firmware: str | None = None
    mcu_firmware: str | None = None
    wlan_driver: str | None = None
    room_location: str | None = None
    brightness: int | None = None
    child_lock: bool | None = None
    night_mode: bool | None = None
    fan_speed: int | None = None
    fan_mode: str | None = None
    filter_expired: bool | None = None
    wifi_working: bool | None = None

    def __post_init__(self):
        _LOGGER.debug(f"Creating Blueair device: {self}")

    async def init(self):
        info = await self.api.get_info(self.uuid)
        self.timezone = info.get("timezone")
        self.compatibility = info.get("compatibility")
        self.model = info.get("model")
        self.firmware = info.get("firmware")
        self.mcu_firmware = info.get("mcuFirmware")
        self.wlan_driver = info.get("wlanDriver")
        self.room_location = info.get("roomLocation")
        self.brightness = info.get("brightness")
        self.child_lock = info.get("child_lock")
        self.night_mode = info.get("night_mode")
        self.fan_speed = info.get("fan_speed")
        self.fan_mode = info.get("fan_mode")
        self.filter_expired = info.get("filter_expired")
        self.wifi_working = info.get("wifi_working")
