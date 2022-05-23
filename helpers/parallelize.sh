while getopts c:j:g:n: flag
do
    case "${flag}" in
        c) cores=${OPTARG};;
        j) job=${OPTARG};;
        g) glob=${OPTARG};;
        n) name=${OPTARG};;
        *) name="job"
    esac
done

for file in $glob; do
    # run jobs in parallele
    if [ $(jobs -r | wc -l) -ge $cores ]; then
        wait $(jobs -r -p | head -1)
    fi
    # start a slow background job here
    (
        echo "$name start $file";
        eval $job;
        echo "$name done ${file##*/}"
    ) &
done
wait # wait for the last job to finish