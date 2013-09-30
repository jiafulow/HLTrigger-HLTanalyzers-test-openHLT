#!/usr/bin/env python
import os, sys, argparse
from datetime import datetime

# own configuration
verbose=True
mprefx="--"
cfgpreamble="#This file has been autogenerated by openHLT.py"
# List of files required for openHLT to run:
#rqfiles=["setup_cff.py"]
logfile="openHLT.log"

#variable definitions and some defaults
ifiles=[]
ofile=[]
maxNrEvents=1000
projectFile=""
hlt_file="hlt.py"
oHLTconfig_template="openHLT.TEMPLATE"
oHLTconfig_out="openhlt_go.py"

# http://docs.python.org/2/library/argparse.html
parser = argparse.ArgumentParser(description='openHLT is a software tool intended to help study and optimize HLT producers and filters.\n\n This script takes openHLT configuration options from the command line, and using a template configuration file, writes out a configuration file which can be run with CMSSW (the openHLT "go" file). See https://twiki.cern.ch/twiki/bin/view/CMS/NewOpenHLT for additional information')

parser.add_argument('-p', '--run-producers', action='store_true', #type=bool,
                    help='run configuration in producer mode (default: False)')

parser.add_argument('-i', '--input-root-files', nargs='+', action='store', metavar='FILES', #type= str,
                    default=ifiles,
                    required=True,
                    help='a space seperated list of input root file(s) (raw data) (required)')

parser.add_argument('-o', '--output-root-file', action='store', metavar='FILE', #type=str,
                    default=ofile,
                    required=True,
                    help="openHLT output root file (required)")

parser.add_argument('-t', '--hlt-config', action='store', metavar='FILE', #type=str,
                    default=hlt_file,
                    #required=True,
                    help="hlt configuration file (default: "+hlt_file+"). Note that the file must be in the same directory with this script.")

parser.add_argument('-c', '--other-changes', nargs='+', action='store', metavar='CHANGES', #type= str,
                    default=["# add additional code below"],
                    required=False,
                    help='a space seperated list of python code strings (each string must be in quotes) to appear in the openHLT go file. Intended as a quick&dirty way to modify module parameters. Strings must have the following form: "process.[module name].[parameter]=cms.[data type]( value )"')

parser.add_argument('-n', '--n-events', action='store', metavar='N',
                    default=maxNrEvents, #type= int,
                    help='maximum number of events to process (default: 1000) Hint: -1 works when in quotes "-1" ')

parser.add_argument('-j', '--crab-job', action='store_true', #type= bool,
                    #default=isCrabJob,
                    help='configuration file will run in a crab job  ')

parser.add_argument('-v', '--verbose', action='store_true', #type= bool,
                    #default=verbose,
                    help='increase verbosity')

parser.add_argument('-l', '--openhlt-template-file', action='store', metavar='FILE', #type=str,
                    default=oHLTconfig_template,
                    #required=True,
                    help="openHLT template file (default: "+oHLTconfig_template+")")

parser.add_argument('-g', '--openhlt-go-file', action='store', metavar='FILE', #type=str,
                    default=oHLTconfig_out,
                    #required=True,
                    help='openHLT "go" file to be written out (default: '+oHLTconfig_out+")")

parser.add_argument('--go', action='store_true', #type= bool,
                    #default=verbose,
                    help='start cmsRun with the "go" file')

parser.add_argument('--mc', dest='is_data', action='store_false', #type= bool,
                    help='run on Monte Carlo simulated events (default: false)')

#parser.add_argument('-m', action='store_true', #type= bool,
#                    #default=verbose,
#                    #go interactive mode
#                    help='reserved')

#parser.add_argument('-a', action='store_true', #type= bool,
#                    #default=verbose,
#                    #read options from a configuration file
#                    help='reserved')

#if projectFile:
#    config = ConfigParser.RawConfigParser()
#    config.read(projectFile)
#    print "read config file"
#    sys.exit()

args = parser.parse_args()

# log the options
with open(logfile, "a") as myfile:
    myfile.write(str(datetime.now()) +" : "+" ".join(sys.argv) +"\n")

try: maxNrEvents=int(args.n_events)
except ValueError:
    print mprefx, parser.prog+": [i] Error:","number of events must be an integer:", args.n_events
    sys.exit()

oHLTconfig_out=args.openhlt_go_file
oHLTconfig_template=args.openhlt_template_file


# Configurations from command line
cmd=('verbose=%r \nisCrabJob=%r  \nrunProducers=%r \nrunOpen=%r \nisData=%r \nifiles=%r \nofile="%s" \nmaxNrEvents=%d'
    % (args.verbose,
       args.crab_job,
       args.run_producers,
       args.run_producers,
       args.is_data,
       args.input_root_files,
       args.output_root_file,
       maxNrEvents))

#print args
hlt_module=args.hlt_config
# check that the file exists and doesn't have zero length
if not os.path.isfile(hlt_module):
    print mprefx,"[!] Error: Cannot find the hlt module:",hlt_module
    sys.exit()
if os.stat(hlt_module)[6]==0:
    # happens when hlt dump fails
    print mprefx,"[!] Error: HLT module file has zero length:",hlt_module
    sys.exit()

if hlt_module[-3:] == ".py":
    hlt_module=hlt_module[:-3]
print mprefx, "[i] HLT module:",hlt_module   

try: temp=open(oHLTconfig_template).read()
except IOError:
    print mprefx,"[!] Error: Cannot find the template file:",oHLTconfig_template
    sys.exit()

if verbose: print mprefx, "[i] read the template file:", oHLTconfig_template
temp=temp.replace("$HLTFILE", hlt_module)
temp=temp.replace("$CONFIG", cmd)
temp=temp.replace("$PATCONFIG", "")

other_changes=""
for change in args.other_changes: other_changes=other_changes+change+"\n"

temp=temp.replace("$OTHERCHANGES", other_changes.strip())
temp=cfgpreamble+"\n"+temp
open(oHLTconfig_out, "w").write(temp)
print mprefx, "[i] wrote:", oHLTconfig_out

# check files required to run openHLT
#goFlag=True
#ls=os.listdir(".")
#for rfile in rqfiles:
#    if rfile not in ls:
#        print mprefx, "[w] a file required to run openHLT not found in the current directory:", rfile
#        goFlag = False

if args.go:
#     if not goFlag:
#        print mprefx, "[w] cannot start cmsRun because at least one of the required files are missing"
#     else:   
        if verbose: print mprefx, "[i] Starting cmsRun"
        cmd="time cmsRun "+oHLTconfig_out
        print cmd
        os.system(cmd)
#print cmd
#print args

