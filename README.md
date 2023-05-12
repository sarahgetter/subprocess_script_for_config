# subprocess_script_for_config
This script uses subprocess.check_output to call bq commands and retrieve their output as strings. 

It then uses json.loads to parse the output of bq ls and bq show --format=json into Python dictionaries. 

Finally, it loops over the datasets and tables and calls the appropriate bq show or bq ls command for each one. 

I chose to have the output printed to the console, but you could also write it to a file or process it in some other way.
