#!/bin/bash
#
# Tim Brooks (brooks@skoorb.net) 2012
# Creates a media page for images and resizes them as needed.
#

EXENAME=${0##*/}

function usage() {
    echo "usage: ${EXENAME} [OPTION] filename"
    echo "Add an image to content/images with medium and thumbnail copys,"
    echo "then adding a markdown page for the image to content/Media"
    echo ""
    echo "  -t TAGS add Tags: TAGS to image markdown"
    echo "  -f      force overwrite of existing page"
}

while getopts ":t:f" Option; do
  case $Option in
    t ) TAGS=$OPTARG ;;
    f ) FORCE=true ;;
    * ) echo "Not recognized argument"; exit -1 ;;
  esac
done
shift $(($OPTIND - 1))

if [ ! -n "$1" ]; then
  usage
  exit 1
fi
if [ ! -f "$1" ]; then
  echo "${EXENAME}: cannot stat \`${1}': No such file or directory"
  exit 1
fi

IMAGENAME=${1##*/}
IMAGEEXT=${IMAGENAME##*.}
IMAGENAME=${IMAGENAME%.*}
PAGEFILE="content/Media/${IMAGENAME}.md"
echo 
if [ ! "$FORCE" -a -f "$PAGEFILE" ]; then
  echo "${EXENAME}: file ${PAGEFILE} already exists; add -f to force overwrite"
  exit 1
fi

IMAGEPATH="content/images/"
mv $1 $IMAGEPATH
cd $IMAGEPATH

echo "Resizing image $IMAGENAME"

convert ${IMAGENAME}.${IMAGEEXT} -resize 1200x800 ${IMAGENAME}_mid.${IMAGEEXT}
convert ${IMAGENAME}.${IMAGEEXT} -resize 400x148 ${IMAGENAME}_thumb.${IMAGEEXT}
echo

cd - > /dev/null
echo "Creating page for image $IMAGENAME"
DATE=`date +%Y-%m-%d\ %H:%m`
TITLE=`echo ${IMAGENAME} | tr '-' ' '`
touch ${PAGEFILE}
echo "Title: $TITLE" > ${PAGEFILE}
if [ "$TAGS" ]; then echo "Tags: ${TAGS}" >> ${PAGEFILE}; fi
echo "Date: ${DATE}" >> ${PAGEFILE}
echo "" >> ${PAGEFILE}
echo "![$TITLE](/static/images/${IMAGENAME}_mid.${IMAGEEXT})" >> ${PAGEFILE}
echo "" >> ${PAGEFILE}
echo "[Click here to download the hi-res version](/static/images/${IMAGENAME}.${IMAGEEXT})" >> ${PAGEFILE}
echo
