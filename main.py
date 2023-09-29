import biotite.database.rcsb as rcsb
import biotite.structure.io.pdb as pdb

# Download a PDB file for demonstration purposes
file_name = rcsb.fetch("mfi_pymol", "pdb", ".")

# Read the PDB file
pdb_file = pdb.PDBFile.read(file_name)

# Get the structure of the protein
# In this case, we are fetching the first model (model=0)
structure = pdb_file.get_structure(model=1)

new_file_name = "mfi.pdb"
new_pdb_file = pdb.PDBFile()
new_pdb_file.set_structure(structure)
new_pdb_file.write(new_file_name)

