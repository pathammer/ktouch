opencv_function_names = [
'cvProjectPoints2',
'cvFindHomography',
'cvCalibrateCamera2',
'cvFindExtrinsicCameraParams2',
'cvRodrigues2',
'cvUndistort2',
'cvInitUndistortMap',
'cvFindChessboardCorners',
'cvDrawChessboardCorners',
'cvRQDecomp3x3',
'cvDecomposeProjectionMatrix',
'cvCreatePOSITObject',
'cvPOSIT',
'cvReleasePOSITObject',
'cvCalcImageHomography',
'cvFindFundamentalMat',
'cvComputeCorrespondEpilines',
'cvConvertPointsHomogenious',
'cvOpenFileStorage',
'cvReleaseFileStorage',
'cvStartWriteStruct',
'cvEndWriteStruct',
'cvWriteInt',
'cvWriteReal',
'cvWriteString',
'cvWriteComment',
'cvStartNextStream',
'cvWrite',
'cvWriteRawData',
'cvWriteFileNode',
'cvGetRootFileNode',
'cvGetFileNodeByName',
'cvGetHashedKey',
'cvGetFileNode',
'char*',
'cvReadInt',
'cvReadIntByName',
'cvReadReal',
'cvReadRealByName',
'char*',
'char*',
'cvRead',
'cvReadByName',
'cvReadRawData',
'cvStartReadRawData',
'cvReadRawDataSlice',
'cvRegisterType',
'cvUnregisterType',
'cvFirstType',
'cvFindType',
'cvTypeOf',
'cvRelease',
'cvClone',
'cvSave',
'cvLoad',
'CV_RGB',
'cvLine',
'cvRectangle',
'cvCircle',
'cvEllipse',
'cvFillPoly',
'cvFillConvexPoly',
'cvPolyLine',
'cvInitFont',
'cvPutText',
'cvGetTextSize',
'cvDrawContours',
'cvInitLineIterator',
'cvClipLine',
'cvEllipse2Poly',
'cvCreateMemStorage',
'cvCreateChildMemStorage',
'cvReleaseMemStorage',
'cvClearMemStorage',
'cvMemStorageAlloc',
'cvMemStorageAllocString',
'cvSaveMemStoragePos',
'cvRestoreMemStoragePos',
'cvCreateSeq',
'cvSetSeqBlockSize',
'cvSeqPush',
'cvSeqPop',
'cvSeqPushFront',
'cvSeqPopFront',
'cvSeqPushMulti',
'cvSeqPopMulti',
'cvSeqInsert',
'cvSeqRemove',
'cvClearSeq',
'cvGetSeqElem',
'cvSeqElemIdx',
'cvCvtSeqToArray',
'cvMakeSeqHeaderForArray',
'cvSeqSlice',
'cvCloneSeq',
'cvSeqRemoveSlice',
'cvSeqInsertSlice',
'cvSeqInvert',
'cvSeqSort',
'cvStartAppendToSeq',
'cvStartWriteSeq',
'cvEndWriteSeq',
'cvFlushSeqWriter',
'cvStartReadSeq',
'cvGetSeqReaderPos',
'cvSetSeqReaderPos',
'cvCreateSet',
'cvSetAdd',
'cvSetRemove',
'cvSetNew',
'cvSetRemoveByPtr',
'cvGetSetElem',
'cvClearSet',
'cvCreateGraph',
'cvGraphAddVtx',
'cvGraphRemoveVtx',
'cvGraphRemoveVtxByPtr',
'cvGetGraphVtx',
'cvGraphVtxIdx',
'cvGraphAddEdge',
'cvGraphAddEdgeByPtr',
'cvGraphRemoveEdge',
'cvGraphRemoveEdgeByPtr',
'cvFindGraphEdge',
'cvFindGraphEdgeByPtr',
'cvGraphEdgeIdx',
'cvGraphVtxDegree',
'cvGraphVtxDegreeByPtr',
'cvClearGraph',
'cvCloneGraph',
'cvCreateGraphScanner',
'cvNextGraphItem',
'cvReleaseGraphScanner',
'cvInitTreeNodeIterator',
'cvNextTreeNode',
'cvPrevTreeNode',
'cvTreeToNodeSeq',
'cvInsertNodeIntoTree',
'cvRemoveNodeFromTree',
'cvGetErrStatus',
'cvSetErrStatus',
'cvGetErrMode',
'cvSetErrMode',
'cvError',
'char*',
'cvRedirectError',
'cvAlloc',
'cvFree',
'cvGetTickCount',
'cvGetTickFrequency',
'cvRegisterModule',
'cvGetModuleInfo',
'cvUseOptimized',
'cvSetMemoryManager',
'cvSetIPLAllocators',
'cvSobel',
'cvLaplace',
'cvCanny',
'cvPreCornerDetect',
'cvCornerEigenValsAndVecs',
'cvCornerMinEigenVal',
'cvCornerHarris',
'cvFindCornerSubPix',
'cvGoodFeaturesToTrack',
'cvExtractSURF',
'cvGetStarKeypoints',
'cvSampleLine',
'cvGetRectSubPix',
'cvGetQuadrangleSubPix',
'cvResize',
'cvWarpAffine',
'cvGetAffineTransform',
'cv2DRotationMatrix',
'cvWarpPerspective',
'cvGetPerspectiveTransform',
'cvRemap',
'cvLogPolar',
'cvCreateStructuringElementEx',
'cvReleaseStructuringElement',
'cvErode',
'cvDilate',
'cvMorphologyEx',
'cvSmooth',
'cvFilter2D',
'cvCopyMakeBorder',
'cvIntegral',
'cvCvtColor',
'cvThreshold',
'cvAdaptiveThreshold',
'cvPyrDown',
'cvPyrUp',
'cvPyrSegmentation',
'cvFloodFill',
'cvFindContours',
'cvStartFindContours',
'cvFindNextContour',
'cvSubstituteContour',
'cvEndFindContours',
'cvMoments',
'cvGetSpatialMoment',
'cvGetCentralMoment',
'cvGetNormalizedCentralMoment',
'cvGetHuMoments',
'cvHoughLines2',
'cvHoughCircles',
'cvDistTransform',
'cvCreateHist',
'cvSetHistBinRanges',
'cvReleaseHist',
'cvClearHist',
'cvMakeHistHeaderForArray',
'cvGetMinMaxHistValue',
'cvNormalizeHist',
'cvThreshHist',
'cvCompareHist',
'cvCopyHist',
'cvCalcHist',
'cvCalcBackProject',
'cvCalcBackProjectPatch',
'cvCalcProbDensity',
'cvEqualizeHist',
'cvMatchTemplate',
'cvMatchShapes',
'cvCalcEMD2',
'cvCheckArr',
'cvKMeans2',
'cvSeqPartition',
'cvAcc',
'cvSquareAcc',
'cvMultiplyAcc',
'cvRunningAvg',
'cvUpdateMotionHistory',
'cvCalcMotionGradient',
'cvCalcGlobalOrientation',
'cvSegmentMotion',
'cvMeanShift',
'cvCamShift',
'cvSnakeImage',
'cvCalcOpticalFlowHS',
'cvCalcOpticalFlowLK',
'cvCalcOpticalFlowBM',
'cvCalcOpticalFlowPyrLK',
'cvCreateKalman',
'cvReleaseKalman',
'CvMat*',
'CvMat*',
'cvCreateConDensation',
'cvReleaseConDensation',
'cvConDensInitSampleSet',
'cvConDensUpdateByTime',
'cvCreateImage',
'cvCreateImageHeader',
'cvReleaseImageHeader',
'cvReleaseImage',
'cvInitImageHeader',
'cvCloneImage',
'cvSetImageCOI',
'cvGetImageCOI',
'cvSetImageROI',
'cvResetImageROI',
'cvGetImageROI',
'cvCreateMat',
'cvCreateMatHeader',
'cvReleaseMat',
'cvInitMatHeader',
'cvMat',
'cvCloneMat',
'cvCreateMatND',
'cvCreateMatNDHeader',
'cvReleaseMatND',
'cvInitMatNDHeader',
'cvCloneMatND',
'cvDecRefData',
'cvIncRefData',
'cvCreateData',
'cvReleaseData',
'cvSetData',
'cvGetRawData',
'cvGetMat',
'cvGetImage',
'cvCreateSparseMat',
'cvReleaseSparseMat',
'cvCloneSparseMat',
'cvGetSubRect',
'cvGetRow',
'cvGetRows',
'cvGetCol',
'cvGetCols',
'cvGetDiag',
'cvGetSize',
'cvInitSparseMatIterator',
'cvGetNextSparseNode',
'cvGetElemType',
'cvGetDims',
'cvGetDimSize',
'cvmGet',
'cvmSet',
'cvClearND',
'cvCopy',
'cvSet',
'cvSetZero',
'cvReshape',
'cvReshapeMatND',
'cvRepeat',
'cvFlip',
'cvSplit',
'cvMerge',
'cvLUT',
'cvConvertScale',
'cvConvertScaleAbs',
'cvAdd',
'cvAddS',
'cvAddWeighted',
'cvSub',
'cvSubS',
'cvSubRS',
'cvMul',
'cvDiv',
'cvAnd',
'cvAndS',
'cvOr',
'cvOrS',
'cvXor',
'cvXorS',
'cvNot',
'cvCmp',
'cvCmpS',
'cvInRange',
'cvInRangeS',
'cvMax',
'cvMaxS',
'cvMin',
'cvMinS',
'cvAbsDiff',
'cvAbsDiffS',
'cvCountNonZero',
'cvSum',
'cvAvg',
'cvAvgSdv',
'cvMinMaxLoc',
'cvNorm',
'cvSetIdentity',
'cvDotProduct',
'cvCrossProduct',
'cvScaleAdd',
'cvGEMM',
'cvTransform',
'cvPerspectiveTransform',
'cvMulTransposed',
'cvTrace',
'cvTranspose',
'cvDet',
'cvInvert',
'cvSolve',
'cvSVD',
'cvSVBkSb',
'cvEigenVV',
'cvCalcCovarMatrix',
'cvMahalanobis',
'cvRound',
'cvSqrt',
'cvInvSqrt',
'cvCbrt',
'cvFastArctan',
'cvIsNaN',
'cvIsInf',
'cvCartToPolar',
'cvPolarToCart',
'cvPow',
'cvExp',
'cvLog',
'cvSolveCubic',
'cvRNG',
'cvRandArr',
'cvRandInt',
'cvRandReal',
'cvDFT',
'cvGetOptimalDFTSize',
'cvMulSpectrums',
'cvDCT',
'cvLoadHaarClassifierCascade',
'cvReleaseHaarClassifierCascade',
'cvHaarDetectObjects',
'cvSetImagesForHaarClassifierCascade',
'cvRunHaarClassifierCascade',
'cvApproxChains',
'cvStartReadChainPoints',
'cvReadChainPoint',
'cvApproxPoly',
'cvBoundingRect',
'cvContourArea',
'cvArcLength',
'cvCreateContourTree',
'cvContourFromContourTree',
'cvMatchContourTrees',
'cvMaxRect',
'cvPointSeqFromMat',
'cvBoxPoints',
'cvFitEllipse2',
'cvFitLine',
'cvConvexHull2',
'cvCheckContourConvexity',
'cvConvexityDefects',
'cvPointPolygonTest',
'cvMinAreaRect2',
'cvMinEnclosingCircle',
'cvCalcPGH',
'cvSubdiv2DGetEdge',
'cvSubdiv2DRotateEdge',
'cvSubdiv2DEdgeOrg',
'cvSubdiv2DEdgeDst',
'cvCreateSubdivDelaunay2D',
'cvSubdivDelaunay2DInsert',
'cvSubdiv2DLocate',
'cvFindNearestPoint2D',
'cvCalcSubdivVoronoi2D',
'cvClearSubdivVoronoi2D',
]
