#Program has to be case-insensitive, can have accidental space either side

# Extension => MIME types
#----------------------------
# .gif => image/gif
# .png => image/png
# .jpg => image/jpeg 
# .jpeg => image/jpeg 
# .txt => text/plain 
# .zip => text/plain 
# .pdf => application/pdf 
# Other suffixes or no suffix at all output "application/octet-stream" 
#----------------------------


file_name = input("File name: ").strip().casefold()  # Makes everything small case and no side spaces
_ , extension = file_name.split(".") # Change the file name into list Ex : cat.jpg => ['cat','jpg']

match extension:

    case "gif":
        mime = "image/gif"
    
    case "png":
        mime = "image/png"
    
    case "jpg" | "jpeg":
        mime = "image/jpeg" 

    case "txt" | "zip":
        mime = "text/plain" 

    case "pdf":
        mime = "application/pdf" 

    case _:
        mime = "application/octet-stream"

print(mime)





