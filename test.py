import AutoUpdate

AutoUpdate.set_url("https://drive.usercontent.google.com/download?id=1-rfCLfxnrRjMQ-WWdAmPbNV6Rpg6dnJQ&export=download&confirm=t&uuid=c8b7463a-45ac-4654-9b0a-f09562b13fa6")
AutoUpdate.set_download_link("https://drive.usercontent.google.com/download?id=1-rfCLfxnrRjMQ-WWdAmPbNV6Rpg6dnJQ&export=download&confirm=t&uuid=c8b7463a-45ac-4654-9b0a-f09562b13fa6")
AutoUpdate.set_current_version("1.0.0")

if not AutoUpdate.is_up_to_date():
    AutoUpdate.download("test1.py")