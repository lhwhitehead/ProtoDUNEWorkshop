# Set up the DUNE software
source /cvmfs/dune.opensciencegrid.org/products/dune/setup_dune.sh
setup dunesw v10_04_05d00 -q e26:prof

# Set up proxy
kx509
voms-proxy-init --noregen -rfc -voms dune:/dune/Role=Analysis

# Set up metacat and rucio for finding files
setup metacat
export METACAT_AUTH_SERVER_URL=https://metacat.fnal.gov:8143/auth/dune
export METACAT_SERVER_URL=https://metacat.fnal.gov:9443/dune_meta_prod/app
setup rucio
