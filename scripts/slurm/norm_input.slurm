#!/bin/bash -l
#SBATCH --job-name="norm_input"
#SBATCH --output=/home/adidishe/EightK/out/norm_input.out
#SBATCH --error=/home/adidishe/EightK/out/norm_input.err
#SBATCH --chdir=/home/adidishe/EightK

# Partition for the job:
#SBATCH --partition=cascade
#SBATCH --account="punim2039"

#SBATCH --mail-type=ALL # notifications for job start, end, and failure
#SBATCH --mail-user=antoine.didisheim@unimelb.edu.au
#SBATCH --mail-type=FAIL
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem=180G
#SBATCH --cpus-per-task=4
#SBATCH --time=0-10:00:00

module load foss/2022a
module load GCCcore/11.3.0; module load Python/3.10.4
module load  cuDNN/8.4.1.50-CUDA-11.7.0
module load TensorFlow/2.11.0-CUDA-11.7.0
source  ~/venvs/nlp_gpu/bin/activate

python3 norm_input.py --news_on_eight=0 --legal=1 --ati=2
