
def ft_tqdm(lst: range) -> None:
    """The function must copy the function tqdm with the yield operator."""

    i = lst.start + 1
    stop = lst.stop
    length_bar = 46
    length = 1
    # duration = int(stop * 0.6) #seconds 199.9
    # frameRate = int((duration / stop) * 10)  #5.5

    for item in lst:
        progress = int(((i + 1) / stop) * 100)
        length = int(length_bar * (progress / 100))
        print(f"{progress}%|[" + '=' * (length) + '>' + ' ' * (length_bar - length) + ']' + f"| {i}/{stop}", end='\r')
        yield item
        i += 1

       #print(end="\x1b[2K") # to clear the output stream
       # print(end="\033[1A") # to go one line up on the output stream
       # end="" # supress the newline
       # end='\r' # to place coursor at the begining of the output stream 
        

