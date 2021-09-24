from pydantic import BaseModel


class DownloadAudioResponse(BaseModel):
    msg: str
    title: str