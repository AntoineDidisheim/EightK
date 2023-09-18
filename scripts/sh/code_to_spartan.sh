#!/usr/bin/env bash
scp *.py adidishe@spartan.hpc.unimelb.edu.au:/home/adidishe/EightK/
scp utils_local/*.py adidishe@spartan.hpc.unimelb.edu.au:/home/adidishe/EightK/utils_local/
scp clean/*.py adidishe@spartan.hpc.unimelb.edu.au:/home/adidishe/EightK/
scp scripts/slurm/* adidishe@spartan.hpc.unimelb.edu.au:/home/adidishe/EightK/
scp summary_stat/* adidishe@spartan.hpc.unimelb.edu.au:/home/adidishe/EightK/

#scp data/raw/crsp_monthly.csv adidishe@spartan.hpc.unimelb.edu.au:/data/gpfs/projects/punim2039/EightK/data/raw/

# Print the current time
echo "Pushed at $(date +'%H:%M')"