#Program has to be case-insensitive, can have accidental space either side

# Extension => MIME types
#----------------------------
# .gif => image/gif
# .png => image/png
# .jpg => image/jpeg 
# .jpeg => image/jpeg 
# .txt => text/plain 
# .zip => application/zip 
# .pdf => application/pdf 
# Other suffixes or no suffix at all output "application/octet-stream" 
#----------------------------


file_name = input("File name: ").strip().casefold()  # Makes everything small case and no side spaces
extension = file_name.split(".")[-1] # Change the file name into list Ex : cat.jpg => ['cat','jpg']

match extension:

    case "gif":
        mime = "image/gif"
    
    case "png":
        mime = "image/png"
    
    case "jpg" | "jpeg":
        mime = "image/jpeg" 

    case "txt":
        mime = "text/plain" 

    case "pdf":
        mime = "application/pdf" 
    
    case "zip":
        mime = "application/zip" 

    case _:
        mime = "application/octet-stream"

print(mime)





