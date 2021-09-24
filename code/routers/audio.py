from fastapi import (APIRouter,
                     Response)
from pytube import YouTube

DOWNLOAD_FILE_PATH = "../../../../Audios/"
router = APIRouter()


@router.get("/download/")
def download_audio(video_id: str):

    yt = YouTube(video_id)

    title = yt.title
    print(f"Video title: {title}")

    audios = yt.streams.filter(only_audio=True)
    ys = audios.get_audio_only()

    ys.download(DOWNLOAD_FILE_PATH)
    print(f"[ {DOWNLOAD_FILE_PATH} ] - Audio is downloaded")

    return Response(content="Download succesfully", status_code=200)   