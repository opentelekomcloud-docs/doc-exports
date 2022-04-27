# doc-exports
Repository to track document exports, not for public use

Document sources (in HTML) are placed under docs/<service_name>/<doc_type>

In the there are files docs_<service_category>.yaml that
describe required data for the particular document. For
all of the documents configured in those files conversion
from HTML to RST will be attempted. In addition to that a
patch file (changes in the RST format) will be generated.

## Automatic pull request proposal

Change for any of the documents configured in the
docs_<service_category>.yaml would trigger job to propose
corresponding changes to the target repository. This is
implemented in the following way:

- HTML content from the pull request will be converted
  with the latest conversion script (otc_doc_convertor) to
RST (new)

- HTML content for the same document from current main
  branch with the corresponding version of the conversion
script will be converted to RST (base).

- **New** state is compared against **base** and
  corresponding patch file is generated

- Resulting patch file is force-applied in the target
  repository (skipping all conflicts) and PR is created

