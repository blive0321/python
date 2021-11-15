import re
from rich.console import Console
from rich.table import Column, Table
from rich import box


console = Console()

INPUT_EXIT_FLAG = 0
while INPUT_EXIT_FLAG != 1:
    
    CHOICE = ""
    DEVICE = ""
    TYPE = ""
    METHOD = ""
    BLOCKSIZE = ""
    QUEUEDEPTH = ""
    THREAD = ""
    TIME = ""
    CRITERIA = ""


    redevice = re.compile('^/dev/.*')
    reblocksize = re.compile('[0-9].*k')
    requeuedepth = re.compile('[0-9]+')
    rethread = re.compile('[0-9]+')
    retime = re.compile('[0-9]+[sh]')
    recriteria = re.compile('[0-9]+MB\/s|[0-9]+k\/IOPS')



    CHOICE = input(" 1. What kind of items you want to test ? (performance | stress) : ")
    if CHOICE != "stress" and CHOICE != "performance":
        console.print("Please enter [green]\"performance\"[/] or [green]\"stress\"[/].\n")
        continue



    DEVICE = input(" 2. Which device you want to test ? (ex: /dev/nvme0n1) : ")
    if not re.fullmatch(redevice,DEVICE):
        console.print("Please enter device name , ex:[green]\"/dev/nvme1n1\"[/].\n")
        continue



    TYPE = input(" 3. Enter which type you want to test (sequential | random) : ")
    if TYPE != "sequential" and TYPE != "random":
        console.print("Please enter [green]\"sequential\"[/] or [green]\"random\"[/].\n")
        continue



    METHOD = input(" 4. Enter which method you want to test (read | write) : ")
    if METHOD != "read" and METHOD != "write":
        console.print("Please enter [green]\"read\"[/] or [green]\"write\"[/].\n")
        continue



    BLOCKSIZE = input(" 5. Enter block size (4k | 128k) : ")
    if not re.fullmatch(reblocksize,BLOCKSIZE):
        console.print("Please enter right block size , ex:[green]\"4k\"[/].\n")
        continue



    QUEUEDEPTH = input (" 6. Enter I/O depths (ex: 1~64) : ")
    if not re.fullmatch(requeuedepth,QUEUEDEPTH):
        console.print("Please enter right queue depth , ex:[green]\"32\"[/].\n")
        continue



    THREAD = input(" 7. Enter thread number (ex: 1~8) : ")
    if not re.fullmatch(rethread,THREAD):
        console.print("Please enter thread number , ex:[green]\"1\"[/].\n")
        continue



    if CHOICE == "stress":
        TIME=input(" 8. Enter testing time : (60s | 1h) : ")
        if not re.fullmatch(retime,TIME):
            console.print("Please enter number plus unit , [green]\"60s\"[/] or [green]\"1h\"[/].\n")
            continue



        CRITERIA=input(" 9. Enter the number of criteria (3000MB/s | 200k/  IOPS) : ")
        if not re.fullmatch(recriteria,CRITERIA):
            console.print("Please enter [green]3000MB/s[/] or [green]200k/IOPS[/].\n")
            continue
        else:
            INPUT_EXIT_FLAG = 1



    elif CHOICE == "performance":
        CRITERIA=input(" 8. Enter the number of criteria (3000MB/s | 200k/IOPS) : ")
        if not re.fullmatch(recriteria,CRITERIA):
            console.print("Please enter [green]3000MB/s[/] or [green]200k/IOPS[/].\n")
            continue
        else:
            INPUT_EXIT_FLAG = 1


print("Jump out the loop")
