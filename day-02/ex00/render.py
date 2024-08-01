
import sys
import os

from settings import name
def render_template(template_file, output_file):
    en = "en"
    try:
        # Check if the template file exists
        if not os.path.exists(template_file):
            print(f"The file '{template_file}' does not exist.")
            return

        # Open the template file in read mode
        with open(template_file, "r") as template:
            # Read the content from the template file
            content = template.read()

        content = content.replace("{name}", name)
        # Open the output file in write mode (this will create the file if it doesn't exist)
        with open(output_file, "w") as output:
            # Write the content to the output file
            output.write("<!DOCTYPE html>\n")
            output.write(f"<html lang={en}>\n")
            output.write(f"<head>\n")
            output.write("    <title>Document</title>\n")
            output.write("</head>\n")
            output.write("<body>\n")
            output.write(content)
            output.write("</body>\n")
            output.write("</html>\n")


        print(f"Content from '{template_file}' has been copied to '{output_file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
  if len(sys.argv) != 2:
      print("Usage: python3 render.py file.template")
  else:
      template_file = sys.argv[1]
      output_file = "myCv.html"  
      render_template(template_file, output_file)
