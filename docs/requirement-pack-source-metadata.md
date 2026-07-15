# Requirement Pack Source Metadata

## Purpose

Requirement packs need enough provenance to show what source they represent, which jurisdiction or organizational scope they belong to, which version was mapped, and who is responsible for reviewing the mapping.

The `source_metadata` object is required for every pack, including synthetic examples.

## Fields

- `authority_name`: issuing authority or synthetic source label
- `source_url`: exact source URL when one exists
- `jurisdiction`: legal, organizational, or not-applicable scope
- `source_version`: version or revision used for the mapping
- `effective_date`: source effective date when applicable
- `review_owner`: role responsible for reviewing and refreshing the mapping
- `review_status`: synthetic, unreviewed, reviewed, or needs-update
- `interpretation_status`: not-applicable, draft-mapping, or reviewed-mapping

## Runtime boundary

Source metadata makes provenance inspectable. It does not prove that:

- the source applies to a particular deployment
- the mapping is legally correct or complete
- the source is still current
- the requirement pack is compliant, certified, approved, or production-ready

A runtime adapter should expose the metadata beside each pack decision so a human or institutional reviewer can identify the source and review route.

## Synthetic examples

The repository's current example packs use:

- `source_type: synthetic_demo`
- `jurisdiction: not_applicable`
- `review_status: synthetic`
- `interpretation_status: not_applicable`

This keeps examples machine-valid without implying that they map a real law, standard, guideline, or organizational policy.
