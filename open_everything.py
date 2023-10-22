import subprocess
import sys


def open_apps(args):
    for app in args:
        match app:
            case "y":
                subprocess.Popen(['C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe', 'www.youtube.com'])
            case "t":
                subprocess.Popen(['C://Program Files//BraveSoftware//Brave-Browser//Application//brave.exe', 'www.twitch.tv'])
            case "d":
                subprocess.Popen(['C://Users//TAI DING//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Discord Inc//Discord.lnk'], shell=True)
            case "s":
                subprocess.Popen(['C://Program Files (x86)//Steam//steam.exe'], shell=True)
            case "v":
                subprocess.Popen(['C://Program Files//Proton//VPN//ProtonVPN.Launcher.exe'], shell=True)


def open_specific_app(args):
    apps = args.split("-")

    for app in apps:
        match app:
            case "riot":
                subprocess.Popen(['C://ProgramData//Microsoft//Windows//Start Menu//Programs//Riot Games//Riot Client.lnk'], shell=True)
            case "valorant":
                subprocess.Popen(['C://ProgramData//Microsoft//Windows//Start Menu//Programs//Riot Games//VALORANT.lnk'], shell=True)
                # Keep in mind vanguard has to be running (i dont want to open it with a script just in case)
            case "insomnia":
                subprocess.Popen(['C://Users//TAI DING//AppData//Local//insomnia//Insomnia.exe'], shell=True)
            case "uni":
                subprocess.Popen(['C://Program Files//Google//Chrome//Application//chrome.exe', 'https://fede.dm/FIUBA-Map/'])
                subprocess.Popen(['C://Program Files//Google//Chrome//Application//chrome.exe', 'https://mli-fiuba.notion.site/Ingenier-a-en-Inform-tica-48e3eeece07e471dbfe1cd947f7ca245'])
                subprocess.Popen(['C://Program Files//Google//Chrome//Application//chrome.exe', 'https://excalidraw.com'])
                subprocess.Popen(['C://Program Files//Google//Chrome//Application//chrome.exe', 'https://campusgrado.fi.uba.ar'])
                subprocess.Popen(['C://Program Files//Google//Chrome//Application//chrome.exe', 'https://guaraniautogestion.fi.uba.ar/g3w/inicio_alumno'])
            case "":
                continue
            case _:
                open_apps(app)


def help():
    print("-- Available args --\n \
            ~short\n \
            y: youtube\n \
            t: twitch\n \
            d: discord\n \
            s: steam\n\n \
            ~spec\n \
            -riot-\n \
            -valorant-\n \
            -insomnia-\n \
            -idea-\n")


def run(args):
    if args == "-help":
        help()
        return
    elif args == "-spec":
        args = sys.argv[2] if len(sys.argv) > 2 else ""
        open_specific_app(args)
        return

    open_apps(args)


if __name__ == "__main__":
    args = sys.argv[1] if len(sys.argv) > 1 else "ytd"
    run(args)
