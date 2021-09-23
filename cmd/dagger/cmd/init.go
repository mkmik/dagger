package cmd

import (
	"os"

	"github.com/spf13/cobra"
	"github.com/spf13/viper"
	"go.dagger.io/dagger/cmd/dagger/cmd/common"
	"go.dagger.io/dagger/cmd/dagger/logger"
	"go.dagger.io/dagger/state"
)

var initCmd = &cobra.Command{
	Use:   "init",
	Short: "Initialize a new empty project",
	Args:  cobra.NoArgs,
	PreRun: func(cmd *cobra.Command, args []string) {
		// Fix Viper bug for duplicate flags:
		// https://github.com/spf13/viper/issues/233
		if err := viper.BindPFlags(cmd.Flags()); err != nil {
			panic(err)
		}
	},
	Run: func(cmd *cobra.Command, args []string) {
		lg := logger.New()
		ctx := lg.WithContext(cmd.Context())

		dir := viper.GetString("project")
		if dir == "" {
			cwd, err := os.Getwd()
			if err != nil {
				lg.
					Fatal().
					Err(err).
					Msg("failed to get current working dir")
			}
			dir = cwd
		}

		project, err := state.Init(ctx, dir)
		if err != nil {
			lg.Fatal().Err(err).Msg("failed to initialize project")
		}

		<-common.TrackProjectCommand(ctx, cmd, project, nil)

	},
}

func init() {
	if err := viper.BindPFlags(initCmd.Flags()); err != nil {
		panic(err)
	}
}
