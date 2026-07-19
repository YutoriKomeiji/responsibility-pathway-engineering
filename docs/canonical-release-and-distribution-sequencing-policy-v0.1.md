# RPE Canonical Release and Distribution Sequencing Policy v0.1

Status: Draft / Human Gate pending

## Purpose

This policy separates continuous public development, implementation verification, package or artifact publication, version tagging, and GitHub Release publication. It prevents an irreversible release record from preceding the canonical executable or distributable artifact.

## Current RPE state

RPE is a Public, continuously inspectable reference-engineering repository. Public visibility and merge to `main` do not make every commit a supported distribution or formal release.

## Canonical artifact decision

Before any formal release, maintainers must declare which artifact is canonical for that release family:

1. **GitHub-release canonical:** the reviewed source snapshot and attached bundles published in the GitHub Release are the primary distribution; or
2. **registry canonical:** a successfully published package or artifact in an external registry is the primary distribution, and the GitHub tag or Release records correspondence after registry publication is confirmed.

The two modes must not be mixed implicitly.

## Common pre-release requirements

1. define release scope, version, supported interfaces, exclusions, and compatibility expectations;
2. identify the candidate commit;
3. run the declared tests, checks, schema validation, examples, build steps, and CI gates;
4. preserve failed, unavailable, warning, and deferred checks alongside successful checks;
5. generate the intended package, bundle, source archive, schema set, manifest, checksums, and release notes as applicable;
6. verify that all generated artifacts correspond to the candidate commit;
7. obtain Human Gate approval for the bounded release candidate.

## GitHub-release canonical sequence

1. complete the common pre-release requirements;
2. create the version tag only after release-candidate approval;
3. create a Draft GitHub Release;
4. attach all intended artifacts and record checksums or manifests where used;
5. verify installation or execution from the staged artifacts where feasible;
6. verify limitations, compatibility, security notes, and non-claims;
7. obtain a final Human Gate;
8. publish the GitHub Release;
9. initiate any secondary mirrors or distributions only after the canonical GitHub Release is confirmed.

## Registry-canonical sequence

1. complete the common pre-release requirements;
2. publish the package or artifact to the selected registry through an explicitly authorized workflow;
3. confirm the registry version, artifact digest, metadata, and availability;
4. record any partial failure or mismatch and stop before creating an immutable release record;
5. create the corresponding version tag only after the canonical registry artifact is confirmed, unless the registry technically requires a pre-existing tag and that exception has been explicitly reviewed;
6. create a Draft GitHub Release referencing the confirmed registry artifact and exact commit;
7. verify metadata, links, hashes, limitations, and correspondence;
8. obtain a final Human Gate;
9. publish the GitHub Release as a record of the already-established canonical artifact.

## Prohibited trigger patterns

Unless an explicit exception is reviewed and documented, the following are prohibited:

- merge to `main` → automatic production or public package publication;
- GitHub Release `published` event → first attempt to create the canonical external package;
- version tag creation → automatic irreversible distribution without a separate approval gate;
- package publication failure → publication of a GitHub Release that implies success;
- release publication → automatic claim of production readiness, safety, compliance, certification, or legal validity;
- RPD baseline release → automatic RPE implementation release.

## Release-state vocabulary

| State | Meaning |
|---|---|
| public-working | inspectable ongoing implementation work |
| candidate | a commit selected for bounded release preparation |
| verified-candidate | declared checks completed with results recorded |
| artifact-staged | distributable artifacts generated but not canonically published |
| canonical-published | the declared canonical artifact is confirmed available |
| tagged | a commit is associated with the confirmed release version |
| release-draft | GitHub Release record and assets are staged |
| released | GitHub Release is published |
| withdrawn-or-superseded | later evidence requires deprecation, correction, or replacement without erasing provenance |

## Failure and recovery

If canonical publication fails, the process stops before GitHub Release publication. The failure record must identify:

- attempted version and commit;
- failed step;
- artifacts that may have become externally visible;
- whether cleanup, yanking, deprecation, or a new version is required;
- the human decision authorizing recovery.

An existing immutable tag or Release must not be silently repointed or recreated. Corrections use an explicit successor version or documented withdrawal path.

## Cross-layer boundary

An RPE release may demonstrate that specified artifacts were built and passed declared checks under stated assumptions. It does not establish production readiness, complete runtime correctness, safety, fairness, legal compliance, certification, operational authorization, or validation of the full RPM → RPD → RPE pathway.

## Human Gate

Canonical-artifact selection, versioning, external registry publication, tag creation, release publication, immutable-release activation, exception approval, withdrawal, and production-use claims remain explicit human decisions.
