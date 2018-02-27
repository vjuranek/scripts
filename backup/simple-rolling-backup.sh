#!/bin/bash

SRC_DIR="/home/vjuranek/dir1"
DEST_DIR="/backup/vjuranek"
NUM_BACKUPS=3

tar -czf $DEST_DIR/backup_`date +%Y-%m-%d-%H-%M`.tgz -C $SRC_DIR .

ACTUAL_BACKUPS=`ls -1 $DEST_DIR/*.tgz|wc -l`
BACKUPS_REMOVE=$(($ACTUAL_BACKUPS-$NUM_BACKUPS))
if [ $BACKUPS_REMOVE -gt 0 ]; then
    for b in `ls -1t $DEST_DIR/*tgz|tail -n $BACKUPS_REMOVE`; do
	rm -rf $b;
    done
fi

