import radical.pilot as rp

## Hard coded path for gromacs --- Can be removed if the variable $PATH is modfiied for the purpose
### MUST BE SET IF THE FOLDER IS NOT ACCESSIBLE 
PATH="/lustre/atlas/proj-shared/csc230/gromacs/gromacs/bin/"

def createGromacsCU(cores,settings):
	'''
	Example -- Creation of a CU descriptor for running gromacs.
	'''
	cu = rp.ComputeUnitDescription() # Create a new CU descriptor
	# Set pre-execution commands
	cu.pre_exec=[]
	# set  the command to run
	cu.executable=["./launcher.sh"] 
	# set the arguments for the executable
	cu.arguments=[settings["output_path"],settings["gromacs_path"]]
	# Stage the input files
	cu.input_staging = [settings["launcher_file"],"topol.tpr"]
	# Set open-mpi
	cu.mpi = True
	# Set the number of cores
	cu.cores=cores
	return cu

def createDateCU():
	'''
	Example -- Creation of a CU descriptor for running /bin/date.
	'''
	cu = rp.ComputeUnitDescription() # Create a new CU descriptor
	# Set pre-execution commands
	cu.pre_exec=[]
	# set  the Command to run
	cu.executable=["/bin/date"] 
	# set the arguments for the executable
	cu.arguments=[]
	# Stage the input files
	cu.input_staging = []
	# Set open-mpi
	cu.mpi = False
	# Set the number of cores
	cu.cores=1
	return cu 
