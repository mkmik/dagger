# Code generated by dagger. DO NOT EDIT.

from typing import NewType

from dagger.client.api import Arg, Type

CacheID = NewType("CacheID", str)
"""
A global cache volume identifier
"""


ContainerID = NewType("ContainerID", str)
"""
A unique container identifier. Null designates an empty container (scratch).
"""


DirectoryID = NewType("DirectoryID", str)
"""
A content-addressed directory identifier
"""


FileID = NewType("FileID", str)

HostDirectoryID = NewType("HostDirectoryID", str)
"""
An identifier for a directory on the host
"""


SecretID = NewType("SecretID", str)
"""
A unique identifier for a secret
"""


class CacheVolume(Type):
    """
    A directory whose contents persist across runs
    """

    def id(self) -> "CacheID":
        _args = []
        _ctx = self._select("id", _args)
        return _ctx.execute(CacheID)


class Container(Type):
    """
    An OCI-compatible container, also known as a docker container
    """

    def build(self, context: DirectoryID, dockerfile: str | None = None) -> "Container":
        """
        Initialize this container from a Dockerfile build
        """
        _args = [
            Arg("context", context),
            Arg("dockerfile", dockerfile, None),
        ]
        _ctx = self._select("build", _args)
        return Container(_ctx)

    def default_args(self) -> "list[str] | None":
        """
        Default arguments for future commands
        """
        _args = []
        _ctx = self._select("defaultArgs", _args)
        return _ctx.execute(list[str] | None)

    def directory(self, path: str) -> "Directory":
        """
        Retrieve a directory at the given path. Mounts are included.
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("directory", _args)
        return Directory(_ctx)

    def entrypoint(self) -> "list[str] | None":
        """
        Entrypoint to be prepended to the arguments of all commands
        """
        _args = []
        _ctx = self._select("entrypoint", _args)
        return _ctx.execute(list[str] | None)

    def env_variable(self, name: str) -> "str | None":
        """
        The value of the specified environment variable
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("envVariable", _args)
        return _ctx.execute(str | None)

    def env_variables(self) -> "EnvVariable":
        """
        A list of environment variables passed to commands
        """
        _args = []
        _ctx = self._select("envVariables", _args)
        return EnvVariable(_ctx)

    def exec(
        self,
        args: list[str] | None = None,
        redirect_stderr: str | None = None,
        redirect_stdout: str | None = None,
        stdin: str | None = None,
    ) -> "Container":
        """
        This container after executing the specified command inside it
        """
        _args = [
            Arg("args", args, None),
            Arg("redirectStderr", redirect_stderr, None),
            Arg("redirectStdout", redirect_stdout, None),
            Arg("stdin", stdin, None),
        ]
        _ctx = self._select("exec", _args)
        return Container(_ctx)

    def exit_code(self) -> "int | None":
        """
        Exit code of the last executed command. Zero means success.
        Null if no command has been executed.
        """
        _args = []
        _ctx = self._select("exitCode", _args)
        return _ctx.execute(int | None)

    def file(self, path: str) -> "File":
        """
        Retrieve a file at the given path. Mounts are included.
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("file", _args)
        return File(_ctx)

    def from_(self, address: str) -> "Container":
        """
        Initialize this container from the base image published at the given address
        """
        _args = [
            Arg("address", address),
        ]
        _ctx = self._select("from", _args)
        return Container(_ctx)

    def fs(self) -> "Directory":
        """
        This container's root filesystem. Mounts are not included.
        """
        _args = []
        _ctx = self._select("fs", _args)
        return Directory(_ctx)

    def id(self) -> "ContainerID":
        """
        A unique identifier for this container
        """
        _args = []
        _ctx = self._select("id", _args)
        return _ctx.execute(ContainerID)

    def mounts(self) -> "list[str]":
        """
        List of paths where a directory is mounted
        """
        _args = []
        _ctx = self._select("mounts", _args)
        return _ctx.execute(list[str])

    def publish(self, address: str) -> "str":
        """
        Publish this container as a new image, returning a fully qualified ref
        """
        _args = [
            Arg("address", address),
        ]
        _ctx = self._select("publish", _args)
        return _ctx.execute(str)

    def stderr(self) -> "File":
        """
        The error stream of the last executed command.
        Null if no command has been executed.
        """
        _args = []
        _ctx = self._select("stderr", _args)
        return File(_ctx)

    def stdout(self) -> "File":
        """
        The output stream of the last executed command.
        Null if no command has been executed.
        """
        _args = []
        _ctx = self._select("stdout", _args)
        return File(_ctx)

    def user(self) -> "str | None":
        """
        The user to be set for all commands
        """
        _args = []
        _ctx = self._select("user", _args)
        return _ctx.execute(str | None)

    def with_default_args(self, args: list[str] | None = None) -> "Container":
        """
        Configures default arguments for future commands
        """
        _args = [
            Arg("args", args, None),
        ]
        _ctx = self._select("withDefaultArgs", _args)
        return Container(_ctx)

    def with_entrypoint(self, args: list[str]) -> "Container":
        """
        This container but with a different command entrypoint
        """
        _args = [
            Arg("args", args),
        ]
        _ctx = self._select("withEntrypoint", _args)
        return Container(_ctx)

    def with_env_variable(self, name: str, value: str) -> "Container":
        """
        This container plus the given environment variable
        """
        _args = [
            Arg("name", name),
            Arg("value", value),
        ]
        _ctx = self._select("withEnvVariable", _args)
        return Container(_ctx)

    def with_fs(self, id: DirectoryID) -> "Container":
        """
        Initialize this container from this DirectoryID
        """
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("withFS", _args)
        return Container(_ctx)

    def with_mounted_cache(self, cache: CacheID, path: str, source: DirectoryID | None = None) -> "Container":
        """
        This container plus a cache volume mounted at the given path
        """
        _args = [
            Arg("cache", cache),
            Arg("path", path),
            Arg("source", source, None),
        ]
        _ctx = self._select("withMountedCache", _args)
        return Container(_ctx)

    def with_mounted_directory(self, path: str, source: DirectoryID) -> "Container":
        """
        This container plus a directory mounted at the given path
        """
        _args = [
            Arg("path", path),
            Arg("source", source),
        ]
        _ctx = self._select("withMountedDirectory", _args)
        return Container(_ctx)

    def with_mounted_file(self, path: str, source: FileID) -> "Container":
        """
        This container plus a file mounted at the given path
        """
        _args = [
            Arg("path", path),
            Arg("source", source),
        ]
        _ctx = self._select("withMountedFile", _args)
        return Container(_ctx)

    def with_mounted_secret(self, path: str, source: SecretID) -> "Container":
        """
        This container plus a secret mounted into a file at the given path
        """
        _args = [
            Arg("path", path),
            Arg("source", source),
        ]
        _ctx = self._select("withMountedSecret", _args)
        return Container(_ctx)

    def with_mounted_temp(self, path: str) -> "Container":
        """
        This container plus a temporary directory mounted at the given path
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withMountedTemp", _args)
        return Container(_ctx)

    def with_secret_variable(self, name: str, secret: SecretID) -> "Container":
        """
        This container plus an env variable containing the given secret
        """
        _args = [
            Arg("name", name),
            Arg("secret", secret),
        ]
        _ctx = self._select("withSecretVariable", _args)
        return Container(_ctx)

    def with_user(self, name: str) -> "Container":
        """
        This container but with a different command user
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("withUser", _args)
        return Container(_ctx)

    def with_workdir(self, path: str) -> "Container":
        """
        This container but with a different working directory
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withWorkdir", _args)
        return Container(_ctx)

    def without_env_variable(self, name: str) -> "Container":
        """
        This container minus the given environment variable
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("withoutEnvVariable", _args)
        return Container(_ctx)

    def without_mount(self, path: str) -> "Container":
        """
        This container after unmounting everything at the given path.
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withoutMount", _args)
        return Container(_ctx)

    def workdir(self) -> "str | None":
        """
        The working directory for all commands
        """
        _args = []
        _ctx = self._select("workdir", _args)
        return _ctx.execute(str | None)


class Directory(Type):
    """
    A directory
    """

    def diff(self, other: DirectoryID) -> "Directory":
        """
        The difference between this directory and an another directory
        """
        _args = [
            Arg("other", other),
        ]
        _ctx = self._select("diff", _args)
        return Directory(_ctx)

    def directory(self, path: str) -> "Directory":
        """
        Retrieve a directory at the given path
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("directory", _args)
        return Directory(_ctx)

    def entries(self, path: str | None = None) -> "list[str]":
        """
        Return a list of files and directories at the given path
        """
        _args = [
            Arg("path", path, None),
        ]
        _ctx = self._select("entries", _args)
        return _ctx.execute(list[str])

    def file(self, path: str) -> "File":
        """
        Retrieve a file at the given path
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("file", _args)
        return File(_ctx)

    def id(self) -> "DirectoryID":
        """
        The content-addressed identifier of the directory
        """
        _args = []
        _ctx = self._select("id", _args)
        return _ctx.execute(DirectoryID)

    def load_project(self, config_path: str) -> "Project":
        """
        load a project's metadata
        """
        _args = [
            Arg("configPath", config_path),
        ]
        _ctx = self._select("loadProject", _args)
        return Project(_ctx)

    def with_copied_file(self, path: str, source: FileID) -> "Directory":
        """
        This directory plus the contents of the given file copied to the given path
        """
        _args = [
            Arg("path", path),
            Arg("source", source),
        ]
        _ctx = self._select("withCopiedFile", _args)
        return Directory(_ctx)

    def with_directory(self, directory: DirectoryID, path: str) -> "Directory":
        """
        This directory plus a directory written at the given path
        """
        _args = [
            Arg("directory", directory),
            Arg("path", path),
        ]
        _ctx = self._select("withDirectory", _args)
        return Directory(_ctx)

    def with_new_file(self, path: str, contents: str | None = None) -> "Directory":
        """
        This directory plus a new file written at the given path
        """
        _args = [
            Arg("path", path),
            Arg("contents", contents, None),
        ]
        _ctx = self._select("withNewFile", _args)
        return Directory(_ctx)

    def without_directory(self, path: str) -> "Directory":
        """
        This directory with the directory at the given path removed
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withoutDirectory", _args)
        return Directory(_ctx)

    def without_file(self, path: str) -> "Directory":
        """
        This directory with the file at the given path removed
        """
        _args = [
            Arg("path", path),
        ]
        _ctx = self._select("withoutFile", _args)
        return Directory(_ctx)


class EnvVariable(Type):
    """
    EnvVariable is a simple key value object that represents an environment variable.
    """

    def name(self) -> "str":
        """
        name is the environment variable name.
        """
        _args = []
        _ctx = self._select("name", _args)
        return _ctx.execute(str)

    def value(self) -> "str":
        """
        value is the environment variable value
        """
        _args = []
        _ctx = self._select("value", _args)
        return _ctx.execute(str)


class File(Type):
    """
    A file
    """

    def contents(self) -> "str":
        """
        The contents of the file
        """
        _args = []
        _ctx = self._select("contents", _args)
        return _ctx.execute(str)

    def id(self) -> "FileID":
        """
        The content-addressed identifier of the file
        """
        _args = []
        _ctx = self._select("id", _args)
        return _ctx.execute(FileID)

    def secret(self) -> "Secret":
        _args = []
        _ctx = self._select("secret", _args)
        return Secret(_ctx)

    def size(self) -> "int":
        """
        The size of the file, in bytes
        """
        _args = []
        _ctx = self._select("size", _args)
        return _ctx.execute(int)


class GitRef(Type):
    """
    A git ref (tag or branch)
    """

    def digest(self) -> "str":
        """
        The digest of the current value of this ref
        """
        _args = []
        _ctx = self._select("digest", _args)
        return _ctx.execute(str)

    def tree(self) -> "Directory":
        """
        The filesystem tree at this ref
        """
        _args = []
        _ctx = self._select("tree", _args)
        return Directory(_ctx)


class GitRepository(Type):
    """
    A git repository
    """

    def branch(self, name: str) -> "GitRef":
        """
        Details on one branch
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("branch", _args)
        return GitRef(_ctx)

    def branches(self) -> "list[str]":
        """
        List of branches on the repository
        """
        _args = []
        _ctx = self._select("branches", _args)
        return _ctx.execute(list[str])

    def tag(self, name: str) -> "GitRef":
        """
        Details on one tag
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("tag", _args)
        return GitRef(_ctx)

    def tags(self) -> "list[str]":
        """
        List of tags on the repository
        """
        _args = []
        _ctx = self._select("tags", _args)
        return _ctx.execute(list[str])


class Host(Type):
    """
    Information about the host execution environment
    """

    def directory(self, id: HostDirectoryID) -> "HostDirectory":
        """
        Access a directory on the host
        """
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("directory", _args)
        return HostDirectory(_ctx)

    def env_variable(self, name: str) -> "HostVariable":
        """
        Lookup the value of an environment variable. Null if the variable is not available.
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("envVariable", _args)
        return HostVariable(_ctx)

    def workdir(self) -> "HostDirectory":
        """
        The current working directory on the host
        """
        _args = []
        _ctx = self._select("workdir", _args)
        return HostDirectory(_ctx)


class HostDirectory(Type):
    """
    A directory on the host
    """

    def read(self) -> "Directory":
        """
        Read the contents of the directory
        """
        _args = []
        _ctx = self._select("read", _args)
        return Directory(_ctx)

    def write(self, contents: DirectoryID, path: str | None = None) -> "bool":
        """
        Write the contents of another directory to the directory
        """
        _args = [
            Arg("contents", contents),
            Arg("path", path, None),
        ]
        _ctx = self._select("write", _args)
        return _ctx.execute(bool)


class HostVariable(Type):
    """
    An environment variable on the host environment
    """

    def secret(self) -> "Secret":
        """
        A secret referencing the value of this variable
        """
        _args = []
        _ctx = self._select("secret", _args)
        return Secret(_ctx)

    def value(self) -> "str":
        """
        The value of this variable
        """
        _args = []
        _ctx = self._select("value", _args)
        return _ctx.execute(str)


class Project(Type):
    """
    A set of scripts and/or extensions
    """

    def extensions(self) -> "Project":
        """
        extensions in this project
        """
        _args = []
        _ctx = self._select("extensions", _args)
        return Project(_ctx)

    def generated_code(self) -> "Directory":
        """
        Code files generated by the SDKs in the project
        """
        _args = []
        _ctx = self._select("generatedCode", _args)
        return Directory(_ctx)

    def install(self) -> "bool":
        """
        install the project's schema
        """
        _args = []
        _ctx = self._select("install", _args)
        return _ctx.execute(bool)

    def name(self) -> "str":
        """
        name of the project
        """
        _args = []
        _ctx = self._select("name", _args)
        return _ctx.execute(str)

    def schema(self) -> "str | None":
        """
        schema provided by the project
        """
        _args = []
        _ctx = self._select("schema", _args)
        return _ctx.execute(str | None)

    def sdk(self) -> "str | None":
        """
        sdk used to generate code for and/or execute this project
        """
        _args = []
        _ctx = self._select("sdk", _args)
        return _ctx.execute(str | None)


class Query(Type):
    def cache_volume(self, key: str) -> "CacheVolume":
        """
        Construct a cache volume for a given cache key
        """
        _args = [
            Arg("key", key),
        ]
        _ctx = self._select("cacheVolume", _args)
        return CacheVolume(_ctx)

    def container(self, id: ContainerID | None = None) -> "Container":
        """
        Load a container from ID.
        Null ID returns an empty container (scratch).
        """
        _args = [
            Arg("id", id, None),
        ]
        _ctx = self._select("container", _args)
        return Container(_ctx)

    def directory(self, id: DirectoryID | None = None) -> "Directory":
        """
        Load a directory by ID. No argument produces an empty directory.
        """
        _args = [
            Arg("id", id, None),
        ]
        _ctx = self._select("directory", _args)
        return Directory(_ctx)

    def file(self, id: FileID) -> "File":
        """
        Load a file by ID
        """
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("file", _args)
        return File(_ctx)

    def git(self, url: str) -> "GitRepository":
        """
        Query a git repository
        """
        _args = [
            Arg("url", url),
        ]
        _ctx = self._select("git", _args)
        return GitRepository(_ctx)

    def host(self) -> "Host":
        """
        Query the host environment
        """
        _args = []
        _ctx = self._select("host", _args)
        return Host(_ctx)

    def http(self, url: str) -> "File":
        """
        An http remote
        """
        _args = [
            Arg("url", url),
        ]
        _ctx = self._select("http", _args)
        return File(_ctx)

    def project(self, name: str) -> "Project":
        """
        Look up a project by name
        """
        _args = [
            Arg("name", name),
        ]
        _ctx = self._select("project", _args)
        return Project(_ctx)

    def secret(self, id: SecretID) -> "Secret":
        """
        Load a secret from its ID
        """
        _args = [
            Arg("id", id),
        ]
        _ctx = self._select("secret", _args)
        return Secret(_ctx)


class Secret(Type):
    """
    A reference to a secret value, which can be handled more safely than the value itself
    """

    def id(self) -> "SecretID":
        """
        The identifier for this secret
        """
        _args = []
        _ctx = self._select("id", _args)
        return _ctx.execute(SecretID)

    def plaintext(self) -> "str":
        """
        The value of this secret
        """
        _args = []
        _ctx = self._select("plaintext", _args)
        return _ctx.execute(str)