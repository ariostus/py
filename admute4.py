print("Loading...")

import asyncio
import pyautogui




TARGET_ID = "Chromium.J3AB5JMWF22VFJFUFAIBDIC7EE";

from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager


async def get_media_info():
    sessions = await MediaManager.request_async()


    # breakpoint()
    
    current_session = sessions.get_current_session()

    if current_session: 
        if current_session.source_app_user_model_id == TARGET_ID:
            info = await current_session.try_get_media_properties_async()

            # song_attr[0] != '_' ignores system attributes
            info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}

            # converts winrt vector to list
            info_dict['genres'] = list(info_dict['genres'])

            return info_dict
        
    await asyncio.sleep(1)
    raise Exception('TARGET_PROGRAM is not the current media session')
    

volume = 1
last_title = ""
def executonier(self):
    global volume, last_title
    
    # print(self)

    title = self["title"]
    checkchek = self["track_number"]

    if title != last_title and checkchek >0:
        print(title)
        last_title = title

    if checkchek == 0 and volume == 1:
        pyautogui.press("volumemute")
        volume = 0
    elif checkchek > 0 and volume == 0:
        pyautogui.press("volumemute")
        volume = 1
    

if __name__ == '__main__':
    run = 1
    print("Hello there!\n")
    while run:
        try:
            current_media_info = asyncio.run(get_media_info())
            executonier(current_media_info)    
            
        except KeyboardInterrupt:
            run = 0
            break
        except:
            continue

        

print("Bye...")
        