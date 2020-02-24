/*
A KBase module: kb_meta_decoder_py2
*/

module kb_meta_decoder_py2 {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    typedef structure {
	string workspace_name;
	string workspace_id;
        string assembly_ref;
        string reads_ref;
    } StrainFinderParams;

    /**
      Finds Strains
    */
    funcdef find_strains(StrainFinderParams params) returns (ReportResults output) authentication required;
};
