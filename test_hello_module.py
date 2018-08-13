import sys
sys.path.append('/Volumes/vv-external-1/Django/python_scripts/modules')
print(sys.path)

import hello

# Call function in module
hello.world()

# Print variable in module
print(hello.shark)

# Call class
jesse = hello.Octopus("Jesse", "Red")
jesse.tell_me_about_octopus()