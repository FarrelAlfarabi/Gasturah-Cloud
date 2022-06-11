import mongoose from 'mongoose';
import bcrypt from 'bcryptjs';
const SALT_WORK_FACTOR = 10;

const UserSchema = mongoose.Schema({
    id: {
        type: 'string',
        required: true,
        unique: true,
    },
    username: {
        type: 'string',
        required: true,
        unique: true,
    },
    
    password: {
        type: 'string',
        required: true
    },
    
    name: {
        type: "string",
    },

    profile_picture: {
        type: "string",
        required: true,
    },

    level: {
        type: "string"
    }

});

UserSchema.pre('save', function (next) {
    const user = this;

    if (user.isModified('password') === false) {
        return next();
    }
    bcrypt.genSalt(SALT_WORK_FACTOR, (err, salt) => {
        if (err) {
            return next(err);
        }

        bcrypt.hash(user.password, salt, (error, hash) => {
            if (error) {
                return next(error);
            }
            user.password = hash;
            return next();
        });
    });
});

UserSchema.statics = {
    valueExists(query) {
        return this.findOne(query).then(result => result);
    }
};

module.exports = mongoose.model('User', UserSchema);
